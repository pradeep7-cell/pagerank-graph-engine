import time
from engine import compute_pagerank
from generator import generate_web_graph


def run_benchmark():
    node_sizes = (500, 2500, 10000, 25000)

    print(f"{'Nodes':<10} | {'Edges':<10} | {'Iterations':<12} | {'Time (s)':<12}")
    print("-" * 52)

    timings = []
    final_ranks = []

    for n in node_sizes:
        edges = generate_web_graph(n)

        t0 = time.perf_counter()
        ranks, iters = compute_pagerank(n, edges)
        elapsed = time.perf_counter() - t0

        timings.append(elapsed)
        final_ranks = ranks
        print(f"{n:<10} | {len(edges):<10} | {iters:<12} | {elapsed:<12.5f}")

    # Rank pages by importance score
    ranked_pages = sorted(enumerate(final_ranks), key=lambda item: item[1], reverse=True)
    print(f"\nTop 5 Authority Pages ({node_sizes[-1]:,}-node network):")
    for rank_idx, (page_id, score) in enumerate(ranked_pages[:5], 1):
        print(f"  #{rank_idx}: Page {page_id:<6} -> Score: {score:.6f}")

    # Verify probability conservation
    print(f"\nTotal Probability Mass Check: {sum(final_ranks):.6f} (Expected: 1.000000)")

    # Print ASCII scaling chart
    print("\nRuntime Scaling Comparison:")
    max_t = max(timings) if timings else 1.0
    for n, t in zip(node_sizes, timings):
        bar = "#" * max(1, int((t / max_t) * 30))
        print(f"  {n:>6} nodes | {bar:<30} ({t:.5f}s)")


if __name__ == "__main__":
    run_benchmark()
