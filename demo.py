from engine import compute_pagerank


def run_search_demo():
    # 1. Define 6 realistic web pages with titles and content
    pages = {
        0: {
            "url": "https://wikipedia.org",
            "title": "Python (programming language) - Wikipedia",
            "content": "python programming language data science algorithms",
        },
        1: {
            "url": "https://python.org",
            "title": "Official Python 3 Documentation",
            "content": "python standard library reference tutorial",
        },
        2: {
            "url": "https://spam-site.xyz",
            "title": "BUY PYTHON PYTHON PYTHON CHEAP NOW!!!",
            "content": "python python python python python click here",
        },
        3: {
            "url": "https://github.com",
            "title": "Trending Python Repositories on GitHub",
            "content": "open source python projects machine learning",
        },
        4: {
            "url": "https://stackoverflow.com",
            "title": "Newest 'python' Questions - Stack Overflow",
            "content": "python programming help code debugging",
        },
        5: {
            "url": "https://random-blog.net",
            "title": "Best South Indian Breakfast Recipes",
            "content": "dosa idli chutney filter coffee recipes",
        },
    }

    # 2. Define directed links (u -> v means page u recommends page v)
    edges = [
        (1, 0),  # Official Docs -> Wikipedia
        (3, 0),  # GitHub -> Wikipedia
        (4, 0),  # StackOverflow -> Wikipedia
        (0, 1),  # Wikipedia -> Official Docs
        (3, 1),  # GitHub -> Official Docs
        (4, 1),  # StackOverflow -> Official Docs
        (0, 4),  # Wikipedia -> StackOverflow
        (1, 4),  # Official Docs -> StackOverflow
        (2, 0),  # Spam site links to Wikipedia, but NO ONE links to Spam site!
        (5, 0),  # Cooking blog links to Wikipedia
    ]

    # 3. Run your PageRank engine
    ranks, iters = compute_pagerank(len(pages), edges)

    print("=" * 65)
    print("  MINI GOOGLE SEARCH ENGINE (POWERED BY YOUR PAGERANK ENGINE)")
    print("=" * 65)
    print(f"Indexed {len(pages)} pages and {len(edges)} hyperlinks in {iters} iterations.\n")

    print("Global Authority Scores (PageRank):")
    for pid, score in sorted(enumerate(ranks), key=lambda x: x[1], reverse=True):
        print(f"  [{score:.4f}] {pages[pid]['url']}")

    # 4. Interactive Search Loop
    print("\nTry searching for: 'python', 'programming', or 'recipes' (type 'exit' to quit)")
    while True:
        query = input("\nSearch Query > ").strip().lower()
        if query in ("exit", "quit", ""):
            break

        # Filter pages matching the keyword, then rank strictly by PageRank score
        matches = []
        for pid, info in pages.items():
            if query in info["content"] or query in info["title"].lower():
                matches.append((ranks[pid], pid, info))

        matches.sort(reverse=True)

        if not matches:
            print(f"  No results found for '{query}'.")
        else:
            print(f"\nShowing {len(matches)} results for '{query}' (Ranked by PageRank):")
            for rank_num, (score, pid, info) in enumerate(matches, 1):
                print(f"  #{rank_num} | {info['title']}")
                print(f"      URL: {info['url']}  (PageRank Score: {score:.4f})")


if __name__ == "__main__":
    run_search_demo()
