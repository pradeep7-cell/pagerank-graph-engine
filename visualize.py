import math
import webbrowser
import os
from engine import compute_pagerank


def generate_html_graph():
    pages = {
        0: "Wikipedia (Python)",
        1: "Python Docs",
        2: "Spam Site",
        3: "GitHub Trending",
        4: "Stack Overflow",
        5: "Cooking Blog",
    }

    edges = [
        (1, 0), (3, 0), (4, 0),
        (0, 1), (3, 1), (4, 1),
        (0, 4), (1, 4),
        (2, 0), (5, 0),
    ]

    ranks, iters = compute_pagerank(len(pages), edges)

    cx, cy, radius = 400, 275, 175
    coords = {}
    for i in range(len(pages)):
        angle = (2 * math.pi * i / len(pages)) - (math.pi / 2)
        coords[i] = (cx + radius * math.cos(angle), cy + radius * math.sin(angle))

    edge_svg = ""
    for u, v in edges:
        x1, y1 = coords[u]
        x2, y2 = coords[v]
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        r_target = 22 + ranks[v] * 105
        end_x = x2 - (dx / dist) * (r_target + 6)
        end_y = y2 - (dy / dist) * (r_target + 6)
        edge_svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{end_x:.1f}" y2="{end_y:.1f}" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />\n'

    node_svg = ""
    for i, label in pages.items():
        x, y = coords[i]
        r = 22 + ranks[i] * 105
        color = "#2563eb" if ranks[i] > 0.2 else "#475569"
        label_y = y + r + 18
        node_svg += f'''
        <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" stroke="#f8fafc" stroke-width="2" />
        <text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" fill="white" font-weight="bold" font-size="11">{ranks[i]:.4f}</text>
        <text x="{x:.1f}" y="{label_y:.1f}" text-anchor="middle" fill="#f8fafc" font-weight="600" font-size="13">{label}</text>
        '''

    html = f"""<!DOCTYPE html>
<html>
<head>
  <title>PageRank Visual Graph</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background: #0f172a; color: #f8fafc; display: flex; flex-direction: column; align-items: center; padding: 20px; }}
    svg {{ background: #1e293b; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.4); }}
  </style>
</head>
<body>
  <h2>PageRank Authority Graph (Converged in {iters} Iterations)</h2>
  <p>Node size is proportional to PageRank score. Blue = High Authority | Grey = Low Authority</p>
  <svg width="800" height="570">
    <defs>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
        <path d="M0,0 L0,6 L9,3 z" fill="#94a3b8" />
      </marker>
    </defs>
    {edge_svg}
    {node_svg}
  </svg>
</body>
</html>"""

    with open("graph.html", "w", encoding="utf-8") as f:
        f.write(html)

    webbrowser.open("file://" + os.path.abspath("graph.html"))


if __name__ == "__main__":
    generate_html_graph()
