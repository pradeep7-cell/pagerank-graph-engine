def compute_pagerank(
    num_nodes: int,
    edges: list,
    damping: float = 0.85,
    tol: float = 1e-6,
    max_iter: int = 100,
):
    """Computes PageRank scores using sparse adjacency lists and power iteration."""
    if num_nodes == 0:
        return [], 0
    if not edges:
        return [1.0 / num_nodes] * num_nodes, 0

    in_links = [[] for _ in range(num_nodes)]
    out_degree = [0 for _ in range(num_nodes)]

    for u, v in edges:
        in_links[v].append(u)
        out_degree[u] += 1

    dangling_nodes = [i for i, deg in enumerate(out_degree) if deg == 0]
    ranks = [1.0 / num_nodes for _ in range(num_nodes)]
    teleport = (1.0 - damping) / num_nodes

    for iteration in range(1, max_iter + 1):
        dangling_sum = sum(ranks[i] for i in dangling_nodes)
        dangling_mass = damping * dangling_sum / num_nodes
        base_score = teleport + dangling_mass

        new_ranks = [0.0 for _ in range(num_nodes)]
        diff = 0.0

        for node in range(num_nodes):
            rank_sum = sum(ranks[src] / out_degree[src] for src in in_links[node])
            updated = base_score + damping * rank_sum
            new_ranks[node] = updated
            diff += abs(updated - ranks[node])

        ranks = new_ranks
        if diff < tol:
            return ranks, iteration

    return ranks, max_iter
