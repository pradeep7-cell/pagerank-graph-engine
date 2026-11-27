# PageRank Graph Analytics Engine

A scalable, zero-dependency Python implementation of Google's **PageRank algorithm** using sparse adjacency lists, power iteration, and preferential attachment network generation.

## Overview
This project models the web as a directed graph $G = (V, E)$ where vertices represent web pages and directed edges represent hyperlinks. It computes the stationary probability distribution of a random surfer traversing the network with damping factor $d = 0.85$ and full dangling-node mass redistribution.

## Mathematical Formulation
At each iteration $k$, the PageRank score $PR(p_i)$ of page $p_i$ is updated via power iteration until L1 convergence ($\|\mathbf{r}^{(k)} - \mathbf{r}^{(k-1)}\|_1 < 10^{-6}$):

$$PR(p_i) = \frac{1 - d}{N} + \frac{d}{N}\sum_{p_j \in D} PR(p_j) + d \sum_{p_j \in M(p_i)} \frac{PR(p_j)}{L(p_j)}$$

* **$N$**: Total number of web pages (nodes)
* **$d = 0.85$**: Damping factor (probability of following an outgoing link)
* **$D$**: Set of dangling nodes (pages with zero outgoing links)
* **$M(p_i)$**: Set of pages linking into $p_i$
* **$L(p_j)$**: Out-degree (number of outgoing links) of page $p_j$

## Project Architecture
* **`engine.py`**: Core sparse PageRank solver utilizing incoming adjacency lists, dangling-node probability redistribution, and L1-norm convergence detection.
* **`generator.py`**: Scale-free directed graph generator simulating realistic web topologies with preferential attachment authority hubs.
* **`main.py`**: End-to-end benchmarking suite measuring runtime scaling, convergence iterations, top authority nodes, and probability conservation.

## Benchmark Results
Evaluated across synthetic scale-free networks from 500 to 25,000 nodes:

| Nodes ($|V|$) | Directed Edges ($|E|$) | Iterations to Converge | Execution Time (s) |
| :--- | :--- | :--- | :--- |
| 500 | 2,220 | 18 | 0.00518s |
| 2,500 | 11,105 | 17 | 0.02769s |
| 10,000 | 44,799 | 18 | 0.12895s |
| 25,000 | 112,808 | 18 | 0.32102s |

* **Top Authority Page (25,000-node network):** Page `13406` (Score: `0.000462`)
* **Probability Conservation Check:** `1.000000` (Verified exact stochastic mass conservation)

## Quick Start
```bash
git clone https://github.com
cd pagerank-graph-engine
python main.py
```
