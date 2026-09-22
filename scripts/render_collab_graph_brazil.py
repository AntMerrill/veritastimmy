#!/usr/bin/env python3
"""Render a focused subgraph of just the Brazilian/Portuguese-language
Collaborators cluster (added 2026-09-21) plus its direct hub/context ties.

Companion to render_collab_graph_clusters.py (which renders the whole
network) - this pulls the same edges/nodes CSVs but restricts to
sandrabronzina, the PORTUGUESE cluster, timballard89/tbfrescue (her direct
hub-side connections), and the original "Original 4" co-tag island (her
other named cluster, kept for dual-membership context) - i.e. Brazil/
Portuguese-language content only, not the Chile/Spanish Expo Family ties
that also touch sandrabronzina.
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
OUT_PNG = os.path.join(BASE, "collab_graph_brazil_cluster_2026-09-21.png")

PORTUGUESE = {
    "ageisianefreitas", "danipinheirodosreis", "diegojjacome", "herbertesmahan",
    "ibelacamargo", "larinoar", "maaydelara", "professordiegocientista",
    "rebecadecastrobatista", "ritamariamatias",
}
ORIGINAL_FOUR = {"actualidadconsoledad", "francoisevenspaul", "freddydice", "sandrabronzina"}
HUBS = {"timballard89"}
CONTEXT = {"tbfrescue"}  # Tim Ballard Foundation Rescue - connects to the Camara dos Deputados posts

FOCUS = PORTUGUESE | ORIGINAL_FOUR | HUBS | CONTEXT

CLUSTER_COLOR = {
    "original_four": "#17becf",
    "portuguese": "#9467bd",
    "hub": "#1f77b4",
    "context": "#8c8c00",
    "unclassified": "#7f7f7f",
}


def classify(handle):
    if handle in HUBS:
        return "hub"
    if handle in CONTEXT:
        return "context"
    if handle == "sandrabronzina":
        return "dual"  # original_four + portuguese, drawn as split wedge
    if handle in ORIGINAL_FOUR:
        return "original_four"
    if handle in PORTUGUESE:
        return "portuguese"
    return "unclassified"


def main():
    with open(EDGES_CSV) as f:
        all_edges = list(csv.DictReader(f))

    G = nx.Graph()
    edge_files = {}
    for row in all_edges:
        s, t = row["source"], row["target"]
        if s in FOCUS and t in FOCUS:
            G.add_edge(s, t)
            edge_files.setdefault((s, t), set()).add(row["file"])

    appearances = {}
    with open(NODES_CSV) as f:
        for row in csv.DictReader(f):
            if row["handle"] in G:
                appearances[row["handle"]] = int(row["appearances"])

    pos = nx.spring_layout(G, seed=11, k=1.3, iterations=300)

    fig, ax = plt.subplots(figsize=(14, 11))
    fig.patch.set_facecolor("white")

    for u, v in G.edges():
        n_posts = len(edge_files[(u, v)]) if (u, v) in edge_files else len(edge_files.get((v, u), []))
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y, color="#b0b0b0", linewidth=1.2 + 0.6 * n_posts, alpha=0.7, zorder=1)

    single_nodes = [n for n in G.nodes if n != "sandrabronzina"]
    for cluster_name, color in CLUSTER_COLOR.items():
        xs, ys, sizes = [], [], []
        for n in single_nodes:
            if classify(n) != cluster_name:
                continue
            xs.append(pos[n][0])
            ys.append(pos[n][1])
            sizes.append(300 + appearances.get(n, 1) * 150)
        if xs:
            ax.scatter(xs, ys, s=sizes, c=color, edgecolors="black", linewidths=0.7, zorder=2)

    if "sandrabronzina" in pos:
        x, y = pos["sandrabronzina"]
        radius = 0.05 + 0.006 * appearances.get("sandrabronzina", 1)
        for i, cname in enumerate(["original_four", "portuguese"]):
            wedge = mpatches.Wedge((x, y), radius, i * 180, (i + 1) * 180,
                                    facecolor=CLUSTER_COLOR[cname],
                                    edgecolor="black", linewidth=0.7, zorder=3)
            ax.add_patch(wedge)

    for n in G.nodes:
        x, y = pos[n]
        ax.annotate(n, (x, y), fontsize=10, ha="center", va="center",
                    xytext=(0, 14), textcoords="offset points", color="#222222")

    legend_handles = [
        mpatches.Patch(color=CLUSTER_COLOR["hub"], label="Primary hub (timballard89)"),
        mpatches.Patch(color=CLUSTER_COLOR["context"], label="tbfrescue (Tim Ballard Foundation Rescue)"),
        mpatches.Patch(color=CLUSTER_COLOR["portuguese"], label="Portuguese/Brazil cluster"),
        mpatches.Patch(color=CLUSTER_COLOR["original_four"], label='"Original 4" (2026-02-07 co-tag island)'),
        mpatches.Patch(facecolor="white", edgecolor="black", label="sandrabronzina = split wedge (dual cluster)"),
    ]
    ax.legend(handles=legend_handles, loc="lower left", fontsize=10, framealpha=0.9)

    ax.set_title("Brazilian/Portuguese-language Collaborators sub-cluster (2026-09-21)", fontsize=15)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, facecolor="white")
    print("wrote", OUT_PNG)
    print(f"\n{len(G.nodes)} nodes, {len(G.edges)} edges in this sub-cluster")


if __name__ == "__main__":
    main()
