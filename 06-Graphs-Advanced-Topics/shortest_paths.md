# Shortest Paths Algorithms

## 1. Dijkstra’s Algorithm

Finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.

**Data Structure:** Priority Queue (Min-Heap).

**Algorithm:**
1.  Initialize distances to all nodes as $\infty$, source to 0.
2.  Push (0, source) to Priority Queue.
3.  While PQ is not empty:
    *   Pop node $u$ with smallest distance.
    *   For each neighbor $v$ of $u$ with weight $w$:
        *   If `dist[u] + w < dist[v]`:
            *   `dist[v] = dist[u] + w`
            *   Push (dist[v], v) to PQ.

**Time Complexity:** $O(E \log V)$.

## 2. Bellman-Ford Algorithm

Finds shortest paths from a source node to all other nodes, even with **negative edge weights**. Can detect negative cycles.

**Algorithm:**
1.  Initialize distances to $\infty$, source to 0.
2.  Relax all edges $V-1$ times.
    *   For each edge $(u, v)$ with weight $w$:
    *   If `dist[u] + w < dist[v]`, update `dist[v]`.
3.  Check for negative cycles: Relax one more time; if any distance changes, a negative cycle exists.

**Time Complexity:** $O(VE)$.

## 3. Floyd-Warshall Algorithm

Finds shortest paths between **all pairs** of nodes.

**Algorithm (Dynamic Programming):**
Let `dist[i][j]` be the shortest distance from $i$ to $j$.
For each intermediate node $k$:
    For each node $i$:
        For each node $j$:
            `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

**Time Complexity:** $O(V^3)$.

## 4. Comparison

| Algorithm | Type | Weights | Complexity | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **Dijkstra** | Single-Source | Non-negative | $O(E \log V)$ | Road Networks (Maps) |
| **Bellman-Ford** | Single-Source | Any (Negative) | $O(VE)$ | Graphs with negative costs |
| **Floyd-Warshall** | All-Pairs | Any | $O(V^3)$ | Dense graphs, small $V$ |

## 5. Real-World Application in CS

### 1. Google Maps
Uses variants of Dijkstra (like A* Search) to find the fastest route.

### 2. Network Routing Protocols
RIP (Routing Information Protocol) uses Bellman-Ford. OSPF (Open Shortest Path First) uses Dijkstra.

## 6. Solved Examples

**Example (Dijkstra):**
Graph: A-B (4), A-C (2), C-B (1).
Start at A.
1.  Dist: A=0, B=$\infty$, C=$\infty$.
2.  Visit A. Neighbors: B(4), C(2). Update B=4, C=2.
3.  Visit C (smallest). Neighbors: B(1). Path A-C-B = 2+1=3. 3 < 4, so Update B=3.
4.  Shortest path to B is 3 via C.

## 7. Practice Problems

1.  Run Dijkstra on a graph with 5 nodes.
2.  Why does Dijkstra fail with negative weights?
3.  Implement Floyd-Warshall for a 4x4 adjacency matrix.
