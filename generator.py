import random


def generate_web_graph(
    num_nodes: int, seed: int = 42
) -> list[tuple[int, int]]:
    """Generates a directed scale-free web graph with authority hubs."""
    rng = random.Random(seed)
    edges: set[tuple[int, int]] = set()

    # Preferential attachment pool (popular pages attract more incoming links)
    target_pool = list(range(num_nodes))

    for src in range(num_nodes):
        num_links = rng.randint(2, 7)
        for _ in range(num_links):
            dst = rng.choice(target_pool)
            if src != dst and (src, dst) not in edges:
                edges.add((src, dst))
                # Increase probability of dst being linked again
                target_pool.append(dst)

    return list(edges)
