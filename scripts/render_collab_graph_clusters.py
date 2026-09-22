#!/usr/bin/env python3
"""Render the collaborators co-tag network with language/region cluster coloring.

Reads inputs/collab/collab_edges.csv + collab_nodes.csv, classifies each
handle into a cluster by best-evidence judgment (account name, known org,
domain, or content already documented in
docs/collaborators_network_2026-09-02.md), and renders a force-directed
graph where node color = cluster and edge color = the cluster shared by
both endpoints (grey if the edge crosses clusters).

Classification confidence is intentionally conservative: a handle only
gets tagged spanish/portuguese/syria if there's a real signal (domain,
known org/personality, on-topic subject matter). Everything else is
"unclassified" (grey) rather than a guessed label.
"""
import csv
import os
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BASE = os.path.expanduser("~/Documents/repos/veritastimmy/inputs/collab")
EDGES_CSV = os.path.join(BASE, "collab_edges.csv")
NODES_CSV = os.path.join(BASE, "collab_nodes.csv")
OUT_PNG = os.path.join(BASE, "collab_graph_clusters_2026-09-21.png")

# --- cluster classification (evidence-based, conservative) ---

SPANISH = {
    "timballardfoundationecuador",  # Ecuador foundation account
    "iglesiasanjosemaria.ec",       # .ec domain, Ecuador church
    "p.juancarlosv",                # Juan Carlos Vasconez, Ecuador (per IG bio)
    "camuees",                      # Centro de Arbitraje y Mediacion (Ecuador legal org)
    "teleamazonasnec",              # Teleamazonas, Ecuadorian TV network
    "estamananate",                 # Spanish-language morning-show-style handle
    "podcastlaplena",               # "La Plena" - Spanish podcast branding
    "eduardoverastegui",            # Eduardo Verastegui, Mexican actor/politician
    "actualidadconsoledad",         # "Actualidad con Soledad" - Spanish news branding
    "paolafelixdiaz",               # Spanish name
    "emilia_maldonadojaramillo",    # Spanish name
    "graciela_noguera_",            # Spanish name
    "denisromeroroa",               # Spanish name
    "encounterministries_mexico",   # explicit "_mexico" suffix
    "andres.fearless",              # Spanish first name "Andres"
    # --- added 2026-09-21, from icloud_pngs_2026-09-21 Collaborators review ---
    "piedradetoqueec",              # .ec-adjacent handle, Ecuador ("Piedra de Toque")
    "filguayaquil",                 # FIL Guayaquil - Ecuador book fair org
    "cambioglobalparadesarrollo_",  # "Cambio Global para el Desarrollo" - Spanish org name
    "dra.carmenpeguero",            # Spanish name/title ("Dra." = Doctora)
    "fabriciolara.ec",              # .ec domain, Ecuador
    "freechildhoodec",              # "ec" suffix, Ecuador (paired with chemalibreria/timballardfoundationecuador)
    "chemalibreria",                # "Chema Libreria" - Ecuador bookstore (Ciencias Sociales)
    "ecuavisatv",                   # Ecuavisa - Ecuadorian TV network
    "ecuavisanoticias",             # Ecuavisa news branding
    "rcnoticiasrd",                 # "RD" = Republica Dominicana (Dominican Republic) news branding
    "expofamily.cl",                # .cl domain, Chile ("Expo Family" event org)
    "margaritarojoc",               # Margarita Rojo, Expo Family Chile panelist
    "dramariajosemancino",          # Dra. Maria Jose Mancino, Expo Family Chile panelist
    "cuerpodextoenlacruz",          # "Cuerpo de Cristo en la Cruz" (CDXC) - Spanish religious org
    "argueta.virginia",             # Virginia Argueta - Spanish surname, same network as sandrabronzina/chemalibreria
    "femineidadvirtuosa",           # "Femineidad Virtuosa" - Spanish phrase branding
}

SYRIA = {
    "western_syria_development",    # named org, the Najib-adjacent account
    "druze_nexus",                  # explicit Druze/Syria subject
    "savedruze",                    # explicit Druze/Syria subject
    "banim3rouf",                   # "Bani Ma'ruf" - Druze in-group self-designation
    "stopalawitegenocide",          # explicit Syria/Alawite subject
    "mansor_ashkar",                # Arabic name, Druze/Syria-cluster adjacent
    "karim.fearless",               # Arabic first name "Karim", Fearless/Syria-adjacent
}

PORTUGUESE = {
    # added 2026-09-21, from icloud_pngs_2026-09-21 Collaborators review -
    # first confirmed Brazil/Portuguese-language nodes with real Collaborators
    # edges (sandrabronzina's Brazil-focused co-tags). sandrabronzina herself
    # stays dual-cluster (original_four + portuguese) via MULTI_CLUSTER below.
    "ritamariamatias",           # Portuguese name, tbfrescue-linked post
    "rebecadecastrobatista",     # Portuguese name, tbfrescue-linked post
    "ibelacamargo",              # sandrabronzina's apparent daughter, Brazil family content
    "ageisianefreitas",          # Geisiane Freitas, Brazilian TV host
    "herbertesmahan",            # Herbert Esmahan, Brazilian TV host
    "larinoar",                  # Larii Souza, Brazil flag emoji in bio, Sao Paulo event
    "maaydelara",                # Mayara de Lara, Sao Paulo bookstore event
    "diegojjacome",              # Brazil's Camara dos Deputados visit
    "professordiegocientista",   # same Camara dos Deputados visit
    "danipinheirodosreis",       # same Camara dos Deputados visit
}

LDS_CRITICAL = {
    "latterdaychad",              # "Latter-day" + critical framing
    "latterdayavenger",           # same
    "nauvoolegion",               # LDS historical militia reference
    "transcendental_mormon_myths",# explicit "mormon_myths"
    "mount_of_olivesids",         # grouped with this cluster per 2026-09-02 writeup
    "ldsabuseonx",                 # added 2026-09-21: explicit "LDS abuse" framing, co-tagged with latterdaychad/transcendental_mormon_myths
}

ORIGINAL_FOUR = {
    # John's own named grouping (2026-09-03) - the standalone 4-node
    # co-tag island from the 2026-02-07 post, kept together as its own
    # named cluster rather than split across spanish/unclassified.
    "actualidadconsoledad",
    "freddydice",
    "sandrabronzina",
    "francoisevenspaul",
}

MULTI_CLUSTER = {
    # nodes with real dual membership - drawn as split-color markers rather
    # than forced into one bucket. actualidadconsoledad is both part of the
    # "Original 4" co-tag island AND genuinely Spanish-language content
    # ("Actualidad con Soledad").
    "actualidadconsoledad": ("original_four", "spanish"),
    # added 2026-09-21: sandrabronzina is both the "Original 4" co-tag island
    # member AND now has a substantial, distinct cluster of real Brazil/
    # Portuguese-language Collaborators edges (family, TV hosts, Camara dos
    # Deputados visit, Sao Paulo events) - a real dual membership, not a guess.
    "sandrabronzina": ("original_four", "portuguese"),
}

CLUSTER_COLOR = {
    "original_four": "#17becf",  # teal, John's named cluster
    "spanish": "#d62728",     # red, per John's requested key
    "syria": "#2ca02c",       # green
    "portuguese": "#9467bd",  # purple (reserved, currently empty - see note)
    "lds_critical": "#ff7f0e",  # orange, per John's request
    "hub": "#1f77b4",         # blue - the two primary Ballard-orbit hub accounts
    "unclassified": "#7f7f7f",  # grey - no confident language/region signal
}

HUBS = {"timballard89", "timballardfoundationecuador"}


def classify(handle):
    if handle in HUBS:
        return "hub"
    if handle in ORIGINAL_FOUR:
        return "original_four"
    if handle in SPANISH:
        return "spanish"
    if handle in SYRIA:
        return "syria"
    if handle in PORTUGUESE:
        return "portuguese"
    if handle in LDS_CRITICAL:
        return "lds_critical"
    return "unclassified"


def main():
    G = nx.Graph()
    edge_dates = {}
    with open(EDGES_CSV) as f:
        for row in csv.DictReader(f):
            s, t = row["source"], row["target"]
            G.add_edge(s, t)
            edge_dates.setdefault((s, t), []).append(row["date"])

    appearances = {}
    with open(NODES_CSV) as f:
        for row in csv.DictReader(f):
            appearances[row["handle"]] = int(row["appearances"])
            if row["handle"] not in G:
                G.add_node(row["handle"])

    clusters = {n: classify(n) for n in G.nodes}

    # Cluster-anchored layout: plain spring_layout on the whole graph lets the
    # hub (connected to nearly everything) dominate and scatters same-cluster
    # nodes apart instead of grouping them. Instead: place each cluster's
    # nodes via their own local spring layout, anchor that cluster around a
    # point on a ring, and put the hub at the centre.
    import math
    import numpy as np

    ring_order = ["spanish", "syria", "lds_critical", "original_four", "unclassified", "portuguese"]
    ring_order = [c for c in ring_order if any(clusters[n] == c for n in G.nodes)]
    n_rings = len(ring_order)
    RING_R = 6.0

    pos = {}
    for h in HUBS:
        if h in G:
            pos[h] = np.array([0.0, 0.0])

    for i, cname in enumerate(ring_order):
        members = [n for n in G.nodes if clusters[n] == cname]
        if not members:
            continue
        angle = 2 * math.pi * i / n_rings
        cx, cy = RING_R * math.cos(angle), RING_R * math.sin(angle)
        sub = G.subgraph(members)
        # local layout: spring if there are internal edges, else circular
        if sub.number_of_edges() > 0:
            local = nx.spring_layout(sub, seed=3, k=0.9, iterations=200)
        else:
            local = nx.circular_layout(sub)
        # scale local layout to a sensible cluster radius based on member count
        local_r = 1.0 + 0.35 * len(members)
        for n, (lx, ly) in local.items():
            pos[n] = np.array([cx + lx * local_r, cy + ly * local_r])

    # any node somehow missed (shouldn't happen) gets dropped near origin
    for n in G.nodes:
        if n not in pos:
            pos[n] = np.array([0.0, 0.0])

    xs_all = [p[0] for p in pos.values()]
    ys_all = [p[1] for p in pos.values()]
    pad = 2.5
    xlim = (min(xs_all) - pad, max(xs_all) + pad)
    ylim = (min(ys_all) - pad, max(ys_all) + pad)

    fig, ax = plt.subplots(figsize=(18, 15))
    fig.patch.set_facecolor("white")

    # edges: color = shared cluster if both endpoints match, else grey "mixed"
    for u, v in G.edges():
        cu, cv = clusters[u], clusters[v]
        if cu == cv and cu != "unclassified":
            color = CLUSTER_COLOR[cu]
            width = 1.8
            alpha = 0.85
        elif "hub" in (cu, cv):
            other = cv if cu == "hub" else cu
            color = CLUSTER_COLOR.get(other, CLUSTER_COLOR["unclassified"])
            width = 1.2
            alpha = 0.5
        else:
            color = "#c7c7c7"
            width = 1.0
            alpha = 0.4
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y, color=color, linewidth=width, alpha=alpha, zorder=1)

    # nodes (multi-cluster nodes drawn as split-color wedges, everything
    # else as a plain scatter dot)
    single_nodes = [n for n in G.nodes if n not in MULTI_CLUSTER]
    for cluster_name, color in CLUSTER_COLOR.items():
        xs, ys, sizes = [], [], []
        for n in single_nodes:
            if clusters[n] != cluster_name:
                continue
            xs.append(pos[n][0])
            ys.append(pos[n][1])
            sizes.append(200 + appearances.get(n, 1) * 120)
        if xs:
            ax.scatter(xs, ys, s=sizes, c=color, edgecolors="black",
                       linewidths=0.6, zorder=2, label=None)

    for n, cluster_names in MULTI_CLUSTER.items():
        if n not in pos:
            continue
        x, y = pos[n]
        radius = 0.28 + 0.03 * appearances.get(n, 1)
        n_slices = len(cluster_names)
        sweep = 360.0 / n_slices
        for i, cname in enumerate(cluster_names):
            wedge = mpatches.Wedge((x, y), radius, i * sweep, (i + 1) * sweep,
                                    facecolor=CLUSTER_COLOR[cname],
                                    edgecolor="black", linewidth=0.6, zorder=3)
            ax.add_patch(wedge)

    for n in G.nodes:
        x, y = pos[n]
        ax.annotate(n, (x, y), fontsize=7.5, ha="center", va="center",
                    xytext=(0, 11), textcoords="offset points",
                    color="#222222")

    legend_handles = [
        mpatches.Patch(color=CLUSTER_COLOR["spanish"], label="Spanish-language cluster (Ecuador/LatAm)"),
        mpatches.Patch(color=CLUSTER_COLOR["syria"], label="Syrian/Druze cluster"),
        mpatches.Patch(color=CLUSTER_COLOR["portuguese"], label="Portuguese/Brazil cluster"),
        mpatches.Patch(color=CLUSTER_COLOR["lds_critical"], label="Disfellowshipped/ex-LDS critical cluster"),
        mpatches.Patch(color=CLUSTER_COLOR["original_four"], label='"Original 4" (2026-02-07 co-tag island)'),
        mpatches.Patch(facecolor="white", edgecolor="black",
                       label="Split wedge = dual cluster membership"),
        mpatches.Patch(color=CLUSTER_COLOR["hub"], label="Primary hub accounts (timballard89 / ...ecuador)"),
        mpatches.Patch(color=CLUSTER_COLOR["unclassified"], label="Unclassified (no confident language/region signal)"),
        mpatches.Patch(color="#c7c7c7", label="Edge crosses clusters"),
    ]
    ax.legend(handles=legend_handles, loc="lower left", fontsize=10, framealpha=0.9)

    ax.set_title("Ballard-network Instagram Collaborators co-tag graph — language/region clusters (updated 2026-09-21)",
                 fontsize=15)
    ax.axis("off")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, facecolor="white")
    print("wrote", OUT_PNG)

    # print cluster membership summary
    from collections import defaultdict
    by_cluster = defaultdict(list)
    for n, c in clusters.items():
        by_cluster[c].append(n)
    for c in ["hub", "spanish", "syria", "lds_critical", "original_four", "portuguese", "unclassified"]:
        members = sorted(by_cluster.get(c, []))
        print(f"\n{c.upper()} ({len(members)}):")
        for m in members:
            print(" -", m)


if __name__ == "__main__":
    main()
