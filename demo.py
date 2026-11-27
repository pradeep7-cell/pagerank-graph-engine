import random
from engine import compute_pagerank
from generator import generate_web_graph


def run_25k_search_engine():
    num_nodes = 25000
    print(f"Building simulated internet of {num_nodes:,} web pages...")
    edges = generate_web_graph(num_nodes, seed=42)
    ranks, iters = compute_pagerank(num_nodes, edges)

    # Assign realistic domains and topics to all 25,000 pages
    topics = {
        "python": ("Python Programming & Data Science", "python programming code algorithms numpy"),
        "ai": ("Artificial Intelligence & Neural Networks", "ai artificial intelligence machine learning deep learning"),
        "blockchain": ("Blockchain Forensics & Crypto Tracing", "blockchain crypto bitcoin ethereum ledger security"),
        "cricket": ("International Cricket Scores & Analytics", "cricket india match scorecard batting bowling"),
        "java": ("Java Enterprise & Data Structures", "java object oriented programming structures algorithms"),
        "movies": ("Cinema Box Office & Film Reviews", "movies cinema film director box office reviews"),
        "recipes": ("South Indian & Global Recipes", "recipes dosa idli cooking food ingredients"),
        "math": ("Linear Algebra & Graph Theory", "mathematics linear algebra matrix eigenvalues graph"),
    }
    domains = ["wikipedia.org", "github.com", "stackoverflow.com", "medium.com", "arxiv.org", "docs.org", "news-daily.net", "blog-hub.xyz"]

    rng = random.Random(42)
    topic_keys = list(topics.keys())
    pages = {}

    for pid in range(num_nodes):
        t_key = rng.choice(topic_keys)
        title_base, keywords = topics[t_key]
        domain = rng.choice(domains)
        pages[pid] = {
            "url": f"https://{domain}/{t_key}/page-{pid}",
            "title": f"{title_base} (Node #{pid})",
            "content": keywords,
        }

    print("=" * 68)
    print(f"  25,000-PAGE SEARCH ENGINE (CONVERGED IN {iters} ITERATIONS)")
    print("=" * 68)
    print("Available topics to search:")
    print("  'python', 'ai', 'blockchain', 'cricket', 'java', 'movies', 'recipes', 'math'")

    while True:
        query = input("\nSearch Query (or 'exit') > ").strip().lower()
        if query in ("exit", "quit", ""):
            break

        matches = []
        for pid, info in pages.items():
            if query in info["content"] or query in info["title"].lower():
                matches.append((ranks[pid], pid, info))

        matches.sort(reverse=True)

        if not matches:
            print(f"  No pages matched '{query}'. Try one of the topics listed above.")
        else:
            print(f"\nFound {len(matches):,} matching pages for '{query}'. Top 5 by PageRank:")
            for rank_num, (score, pid, info) in enumerate(matches[:5], 1):
                print(f"  #{rank_num} | {info['title']}")
                print(f"      URL: {info['url']}  |  PageRank: {score:.6f}")


if __name__ == "__main__":
    run_25k_search_engine()
