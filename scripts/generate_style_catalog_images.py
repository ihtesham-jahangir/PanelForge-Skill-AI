#!/usr/bin/env python3
"""Generate lightweight, repository-owned SVG references for every catalog style."""

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "images" / "styles"

STYLES = [
    ("skeuomorphism", "Skeuomorphism", "#d9c3a5", "#684d3c", "#f7efe3", "Tactile surfaces"),
    ("minimalism", "Minimalism", "#f5f5f2", "#1d2329", "#ffffff", "Quiet hierarchy"),
    ("glassmorphism", "Glassmorphism", "#12233f", "#8ce3ff", "#253d63", "Layered context"),
    ("claymorphism", "Claymorphism", "#f6d8d0", "#6f3f5b", "#fff4ef", "Soft objects"),
    ("neumorphism", "Neumorphism", "#d8dee8", "#334155", "#e7ebf1", "Inset controls"),
    ("neo-brutalism", "Neo-brutalism", "#ffe34d", "#111111", "#fff7b2", "Bold structure"),
    ("bento-grid", "Bento Grid", "#e9eef8", "#1e3a8a", "#ffffff", "Modular grouping"),
    ("retro-y2k", "Retro Y2K", "#d8b4fe", "#32145f", "#f0fdff", "Digital nostalgia"),
    ("liquid-glass", "Liquid Glass", "#102a43", "#7cf5d2", "#1d496b", "Fluid surfaces"),
    ("flat-design", "Flat Design", "#e9f5ff", "#145da0", "#ffffff", "Direct feedback"),
    ("material-design", "Material Design", "#edf2f7", "#1565c0", "#ffffff", "Elevation roles"),
    ("material-you", "Material You", "#f5e9ff", "#6b21a8", "#fff8ff", "Adaptive theming"),
    ("fluent-design", "Fluent Design", "#e8f1fb", "#0f6cbd", "#ffffff", "Enterprise clarity"),
    ("swiss-style", "Swiss Style", "#f1f1ef", "#e21d48", "#ffffff", "Rational grid"),
    ("editorial-design", "Editorial Design", "#f4ede4", "#7c2d12", "#fffaf3", "Narrative hierarchy"),
    ("brutalism", "Brutalism", "#f4f0e8", "#000000", "#ffffff", "Raw directness"),
    ("dark-oled", "Dark OLED", "#050608", "#b8ff5a", "#111318", "Power-efficient dark"),
    ("cyberpunk", "Cyberpunk", "#100b2e", "#ff2bd6", "#1d1549", "Technical energy"),
    ("retro-futurism", "Retro-futurism", "#e8ddc8", "#a23e2a", "#f8f2e7", "Analog future"),
    ("organic-ui", "Organic UI", "#e9f0df", "#3f6212", "#f8fcf0", "Natural rhythm"),
    ("maximalism", "Maximalism", "#fff1d6", "#c026d3", "#ffe4e6", "Expressive abundance"),
    ("gradient-mesh", "Gradient Mesh", "#e0e7ff", "#4338ca", "#fff1f2", "Atmospheric fields"),
    ("aurora-ui", "Aurora UI", "#dffaf2", "#087f5b", "#eff6ff", "Ambient emphasis"),
    ("data-dense-enterprise", "Data-dense Enterprise UI", "#e5e7eb", "#1f2937", "#f9fafb", "Operational accuracy"),
    ("motion-first-ui", "Motion-first UI", "#e0f2fe", "#0369a1", "#ffffff", "State continuity"),
    ("ai-native-interfaces", "AI-native Interfaces", "#ede9fe", "#4338ca", "#ffffff", "Controllable collaboration"),
]


def svg(slug: str, title: str, background: str, ink: str, surface: str, motif: str) -> str:
    safe_title = escape(title)
    safe_motif = escape(motif)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 700" role="img" aria-labelledby="title desc">
  <title id="title">{safe_title} dashboard example</title>
  <desc id="desc">A PanelForge admin dashboard reference showing the {safe_title} visual style: {safe_motif}.</desc>
  <defs>
    <linearGradient id="wash" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="{background}"/>
      <stop offset="1" stop-color="{surface}"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-opacity=".14"/>
    </filter>
  </defs>
  <rect width="1200" height="700" rx="28" fill="url(#wash)"/>
  <rect x="34" y="34" width="1132" height="632" rx="20" fill="{surface}" stroke="{ink}" stroke-opacity=".16"/>
  <rect x="34" y="34" width="215" height="632" rx="20" fill="{ink}" fill-opacity=".92"/>
  <text x="66" y="88" fill="{surface}" font-family="Arial,sans-serif" font-size="21" font-weight="700">PANELFORGE</text>
  <text x="66" y="126" fill="{surface}" fill-opacity=".65" font-family="Arial,sans-serif" font-size="13">{safe_title}</text>
  <g fill="{surface}" fill-opacity=".78" font-family="Arial,sans-serif" font-size="15">
    <text x="66" y="190">Overview</text><text x="66" y="234">Analytics</text>
    <text x="66" y="278">Customers</text><text x="66" y="322">Billing</text>
    <text x="66" y="366">Audit log</text>
  </g>
  <rect x="276" y="68" width="846" height="56" rx="14" fill="{background}" fill-opacity=".74"/>
  <circle cx="311" cy="96" r="13" fill="{ink}" fill-opacity=".86"/>
  <text x="342" y="103" fill="{ink}" font-family="Arial,sans-serif" font-size="22" font-weight="700">Operations overview</text>
  <circle cx="1070" cy="96" r="17" fill="{ink}" fill-opacity=".15"/>
  <text x="1092" y="102" fill="{ink}" font-family="Arial,sans-serif" font-size="14">Admin</text>
  <g filter="url(#shadow)">
    <rect x="276" y="152" width="196" height="112" rx="16" fill="{surface}" stroke="{ink}" stroke-opacity=".12"/>
    <rect x="492" y="152" width="196" height="112" rx="16" fill="{surface}" stroke="{ink}" stroke-opacity=".12"/>
    <rect x="708" y="152" width="196" height="112" rx="16" fill="{surface}" stroke="{ink}" stroke-opacity=".12"/>
    <rect x="924" y="152" width="198" height="112" rx="16" fill="{ink}" fill-opacity=".92"/>
  </g>
  <g font-family="Arial,sans-serif">
    <g fill="{ink}" font-size="13" opacity=".72"><text x="298" y="183">Active users</text><text x="514" y="183">Conversion</text><text x="730" y="183">Revenue</text></g>
    <g fill="{ink}" font-size="29" font-weight="700"><text x="298" y="226">12,842</text><text x="514" y="226">8.46%</text><text x="730" y="226">$48.2k</text></g>
    <text x="946" y="183" fill="{surface}" fill-opacity=".7" font-size="13">Health score</text>
    <text x="946" y="226" fill="{surface}" font-size="29" font-weight="700">98.4</text>
  </g>
  <rect x="276" y="292" width="500" height="330" rx="16" fill="{surface}" stroke="{ink}" stroke-opacity=".12"/>
  <text x="302" y="330" fill="{ink}" font-family="Arial,sans-serif" font-size="18" font-weight="700">Weekly performance</text>
  <g stroke="{ink}" stroke-opacity=".1"><path d="M302 382H748M302 438H748M302 494H748M302 550H748"/></g>
  <path d="M304 532 C360 500 382 510 424 458 S490 462 530 422 S592 452 632 382 S698 406 748 350" fill="none" stroke="{ink}" stroke-width="8" stroke-linecap="round"/>
  <circle cx="748" cy="350" r="8" fill="{ink}"/>
  <rect x="800" y="292" width="322" height="330" rx="16" fill="{surface}" stroke="{ink}" stroke-opacity=".12"/>
  <text x="826" y="330" fill="{ink}" font-family="Arial,sans-serif" font-size="18" font-weight="700">Recent activity</text>
  <g font-family="Arial,sans-serif" font-size="14" fill="{ink}">
    <circle cx="832" cy="378" r="7" fill="{ink}"/><text x="854" y="383">Role updated</text><text x="854" y="404" opacity=".58">2 minutes ago</text>
    <circle cx="832" cy="450" r="7" fill="{ink}" fill-opacity=".7"/><text x="854" y="455">Invoice paid</text><text x="854" y="476" opacity=".58">18 minutes ago</text>
    <circle cx="832" cy="522" r="7" fill="{ink}" fill-opacity=".45"/><text x="854" y="527">New workspace</text><text x="854" y="548" opacity=".58">1 hour ago</text>
  </g>
  <text x="276" y="652" fill="{ink}" fill-opacity=".6" font-family="Arial,sans-serif" font-size="12">{safe_motif} · accessible fallback · responsive layout</text>
</svg>
"""


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for style in STYLES:
        (OUTPUT / f"{style[0]}.svg").write_text(svg(*style), encoding="utf-8")
    print(f"Generated {len(STYLES)} style catalog SVGs in {OUTPUT}")


if __name__ == "__main__":
    main()
