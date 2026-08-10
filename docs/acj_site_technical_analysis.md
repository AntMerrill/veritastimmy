# americancrimejournal.com — Technical Analysis

**Date:** 2026-08-10
**Method:** passive/read-only reconnaissance only — HTTP headers, DNS, WHOIS,
robots.txt/sitemaps, WP REST API, and static analysis of the HTML already
pulled from the site during the ACJ sub-archive crawl. No login attempts, no
scanning, nothing that touches non-public endpoints.

## TL;DR

ACJ runs on **WordPress.com "Atomic" hosting** — Automattic's own
infrastructure, end to end: registrar, DNS, TLS cert, CDN, and hosting are
all Automattic. It's a real, actively-maintained news site (Brotli
compression, image CDN, auto-generated sitemaps), but the HTML is
widget-bloated (645 `<h3>` tags on the homepage, almost all boilerplate),
security headers are minimal beyond HSTS, and it's running a **beta**
version of Jetpack in production.

## Hosting & Infrastructure

| Item | Value |
|---|---|
| Domain created | 2019-03-13 (per WHOIS) |
| Domain expires | 2027-03-13 |
| Domain last updated | 2026-02-21 |
| Registrar | **Automattic Inc.** (WordPress.com's parent company — they own the domain registration itself, not just the hosting) |
| Nameservers | `ns1/ns2/ns3.wordpress.com` |
| A records | `192.0.78.170`, `192.0.78.229` (Automattic/WordPress.com IP block) |
| MX records | Google Workspace (`aspmx.l.google.com` + alts) — email is on Gmail/Workspace, separate from the WP.com stack |
| Web server | `nginx`, fronted by Automattic's own CDN (`server-timing: a8c-cdn`, datacenter `sjc` = San Jose) |
| Platform tell | `host-header: WordPress.com` + `x-ac` header confirm **WordPress.com Atomic** hosting (self-managed-WP-grade features running on WP.com's infra, not a plain WordPress.com blog) |
| Easter egg | `x-hacker: Want root? Visit join.a8c.com and mention this header.` — Automattic's standard recruiting header, appears on all their Atomic-hosted sites |

## TLS

- Certificate CN: `tls.automattic.com` — a **shared wildcard-style cert**
  covering many Automattic-hosted domains, not one issued specifically to
  americancrimejournal.com.
- Issuer: Google Trust Services (`WR1`).
- Validity: 2026-06-28 → 2026-09-26 (~90-day rotation, auto-renewed —
  standard for this class of managed cert).
- HSTS is set (`max-age=31536000`), so browsers will force HTTPS on repeat
  visits.

## CMS & Plugin Stack

Confirmed via `wp-json/`, HTML source references, and generator meta tags:

- **CMS:** WordPress (WordPress.com Atomic)
- **Theme:** `bestwp-pro` (a commercial news/magazine theme — its sidebar
  widget classes, e.g. `bestwp-side-widget`, `bestwp-fp01-post-*`, are all
  over the homepage and sub-archive pages)
- **Plugins detected:**
  - **Jetpack — v16.1-beta.3.** Running a beta build in production is the
    single most notable finding here; worth a heads-up to Damion since beta
    plugin builds occasionally regress on production sites.
  - Jetpack Boost (performance — injects per-block critical CSS)
  - Gutenberg (block editor, layered on top of WP core's built-in one)
  - Yoast SEO v28.2
  - Akismet (comment/form spam filtering)
  - MailPoet (newsletter/email)
  - CoBlocks
  - **Newspack Blocks** — Automattic's block library purpose-built for news
    orgs, consistent with ACJ's investigative-journalism format
  - VideoPress
  - Google Site Kit v1.183.0 (this actually showed up as the page's
    `<meta name="generator">` tag, ahead of any WordPress-specific tag)
  - Regenerate Thumbnails
  - A `woocommerce-email-editor/v1` REST namespace is registered, but there's
    no visible storefront on the site — likely a bundled dependency of
    another plugin rather than an active shop.

## REST API / Endpoint Exposure

- `wp-json/` is fully open and lists ~25 namespaces (Jetpack, Yoast, AMP,
  Blaze, VideoPress, etc.) — normal for a WP.com Atomic site, not a
  misconfiguration by itself.
- `wp-json/wp/v2/users` is public but returns only a **single generic
  account** (`ACJ Staff`, id `140309370`) — bylines like "Damion Moore" are
  already public via article author pages anyway, so this isn't leaking
  anything beyond what's already visible in normal browsing.
- `xmlrpc.php` → **403** and `wp-login.php` → **403** — both blocked at the
  platform level. WP.com Atomic sites route auth through wordpress.com
  itself rather than the classic `wp-login.php` form, so this is expected
  hardening, not a bug.
- `readme.html` → **200** (the generic stock WordPress readme, not
  ACJ-specific) — technically an information-disclosure hygiene miss
  (best practice is to block/remove it), but in this case it doesn't leak a
  usable core version string, so the actual exposure is minimal.

## Where images live

- Canonical originals sit at the standard WordPress path:
  `/wp-content/uploads/YYYY/MM/filename.ext` (confirmed directly resolvable,
  200 OK, not blocked).
- Actually **served** through Jetpack's **Photon** image CDN at
  `i0.wp.com/americancrimejournal.com/wp-content/uploads/...` — this is what
  every `<img>` tag on the site actually points to.
- Photon behavior observed on a sample image:
  - On-the-fly resizing via query params (`?resize=480%2C240`)
  - Aggressive caching: `cache-control: public, max-age=63115200` (~2 years),
    `expires` set 2 years out
  - Automatic recompression: `x-bytes-saved: 94167` (this one PNG had ~62%
    shaved off it)
  - Wide-open CORS: `access-control-allow-origin: *`
- Image, video, and page sitemaps are all auto-generated by Jetpack
  (`image-sitemap-*.xml`, `video-sitemap-*.xml`, `sitemap-*.xml`), listed
  from `robots.txt` and `sitemap_index.xml` — both routine SEO plumbing, no
  surprises.

## HTML / frontend quality

- Valid HTML5 (`<!DOCTYPE html>`), `lang="en-US"` set, responsive viewport
  meta present — the basics are correct.
- **Page weight:** homepage HTML is ~1.98 MB uncompressed but only ~173 KB
  over the wire (Brotli, ~11:1 ratio) — the raw markup is bloated but actual
  bandwidth cost to a visitor is reasonable.
- **Heading structure is a real smell:** homepage has 2× `<h1>`, 10× `<h2>`,
  and **645× `<h3>`**. The `<h3>` explosion is almost entirely repeated
  sidebar widgets (RSS feed items, "featured post" cards) rather than actual
  content hierarchy — this dilutes semantic structure and would make
  screen-reader heading-navigation nearly unusable on that page.

  *Why it matters:* screen-reader users commonly navigate by jumping
  heading-to-heading. On this homepage that list is ~99% boilerplate widget
  titles before reaching any real content heading — it defeats headings as
  a navigation aid, and muddies the page outline for SEO crawlers too.

  *How it'd normally be fixed* (theme-level, inside `bestwp-pro`'s
  templates — not something ACJ's editors control per-post):

  1. Stop treating every repeated widget entry as its own heading. A
     sidebar's own title ("Unresolved Podcast," "Recent Articles") can
     reasonably be one `<h3>`/`<h4>`, but the individual post-title links
     inside it should just be plain text/links (`<p>` or `<span>`, styled
     to look identical) — not a heading each.
  2. Reserve heading levels for actual document structure, incrementing
     sensibly (h1 → page title, h2 → major sections, h3 → subsections
     within those), rather than reusing h3 as a catch-all style class.
  3. Wrap sidebars in `<aside role="complementary">` landmarks so
     assistive tech can skip past them via landmark navigation instead of
     relying on heading-hopping.

  This requires a child-theme override or a theme update — not fixable
  from the WordPress admin UI alone.
- **CSS delivery:** zero external `<link rel="stylesheet">` tags; instead 26
  separate inline `<style>` blocks (Jetpack Boost injecting per-block
  "critical CSS"). Good for first paint, bad for cross-page CSS caching —
  a real trade-off, not obviously a mistake.
- **JS footprint is lean:** only 6 external `<script src="">` tags on the
  homepage.
- **Accessibility gap:** on the O.U.R. hub page, 1 of 10 `<img>` tags had no
  `alt` attribute at all.
- **Performance:** TTFB ~313ms, full response ~613ms for the homepage on a
  cold cache. The O.U.R. archive hub page specifically showed a 5.1s
  server-side render time on cache MISS (`server-timing: ... cache;desc=MISS;dur=5148.0`)
  during this crawl — that page is comparatively expensive to (re)build,
  likely due to its size/widget count, though it's fast once cached.

## Security headers

| Header | Present? |
|---|---|
| `Strict-Transport-Security` | Yes (`max-age=31536000`) |
| `Content-Security-Policy` | No |
| `X-Frame-Options` | No |
| `X-Content-Type-Options` | No on HTML responses (present on Photon image responses only) |
| `Referrer-Policy` | No |
| `Permissions-Policy` | No |

HSTS is the only hardening header on document responses. The absence of a
CSP/X-Frame-Options is a real theoretical clickjacking exposure, though
WP.com's platform likely compensates with edge-level protections not
visible in these headers.

## Overall characterization: more than a blog, less than a newsroom

Structurally, ACJ sits in a specific, identifiable tier: a small independent
investigative outlet running on a professional-but-off-the-shelf WordPress
stack — more than a hobby blog, but not a newsroom with a dedicated
engineering team.

**What pushes it past "just a blog":**

- **Atomic/Business-tier WP.com hosting**, not a free wordpress.com blog —
  that tier costs money specifically because it allows custom plugins/themes
  and shell access, so someone's investing real money in the infrastructure.
- **Newspack Blocks** plugin — Automattic's product line built specifically
  for newsrooms (the broader Newspack initiative targets local/independent
  news orgs, often with Google News Initiative backing). Its presence
  signals ACJ is using tooling aimed at publishers, not bloggers.
- **Editorial apparatus:** a dedicated Editorial Standards page, a
  Corrections Policy page, and named contributors with bios (Damion Moore,
  Lynn Packer as "special contributor," Dr. Laura Robinson) — the kind of
  self-governance structure a real publication maintains that a personal
  blog typically doesn't bother with.
- **Multi-channel distribution:** newsletter (MailPoet), in-house video
  hosting (VideoPress) rather than just YouTube embeds, a cross-promoted
  podcast ("Unresolved," via RSS), Patreon monetization, and presence on
  five-plus social platforms (X, Bluesky, Threads, Instagram, Facebook,
  YouTube).
- **The actual work product:** multi-year investigative series with
  primary-source court filings, IRS Form 990s, and depositions — original
  reporting infrastructure, which is exactly why this archive was worth
  mining in the first place.

**What keeps it small-scale:**

- One WordPress install running a commercial theme (`bestwp-pro`), not
  custom-built platform engineering.
- Byline concentration around essentially one or two people, not a staffed
  newsroom.
- No paywall/ad infrastructure — monetization is external (see below).
- Everything lives inside the WP monolith — no separate app or backend.

## Monetization / can Damion collect money?

**Currently active:** yes, via **Patreon**
(`patreon.com/americancrimejournal`), linked directly from the site. This is
handled entirely off-platform — Patreon does its own payment processing
(cards, PayPal, etc.), not WordPress.

**Not currently active, but technically available given the stack:**

- **Jetpack Payments/Donations block** — since Jetpack is already active, a
  Stripe-backed donation or recurring-payment block could be added directly
  to any page/post without additional hosting changes.
- **WooCommerce** — a `woocommerce-email-editor/v1` REST namespace is
  registered (seen in the `wp-json/` route list), meaning some WooCommerce
  component is installed, but there's no visible storefront or products
  anywhere on the site. This is most likely a leftover dependency pulled in
  by another plugin rather than an active shop. His Business/Commerce-tier
  hosting does support standing up a real WooCommerce store if he wanted
  one.

Net: money collection today is entirely external (Patreon); WordPress-native
payment options exist in the stack but appear unused.

## Things worth flagging to Damion

1. **Jetpack is on a beta build (16.1-beta.3) in production** — worth
   checking whether that's intentional (opted into a beta channel) or
   accidental.
2. **People / Organizations & Network sections have no working links**
   (already reported separately — see `ACJ_HOLDINGS.md` and
   `acj_remaining_subarchives_report.md`).
3. No CSP/X-Frame-Options/Referrer-Policy on document responses — low
   priority given the platform, but easy to add via Jetpack/theme config if
   he wants a hardening pass.
4. `readme.html` is publicly reachable — cosmetic info-disclosure hygiene
   item, doesn't leak anything meaningful here but is trivial to block.
