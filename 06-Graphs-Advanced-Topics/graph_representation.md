# Graph Representation

## 1. Introduction

How do we store a graph in a computer? The choice of representation affects algorithm performance.

## 2. Adjacency Matrix

A 2D array of size $V \times V$ where $A[i][j] = 1$ if there is an edge from $i$ to $j$, and 0 otherwise.

*   **Space Complexity:** $O(V^2)$
*   **Check Edge:** $O(1)$
*   **Iterate Neighbors:** $O(V)$

**Example:**
$$
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 1 \\
0 & 1 & 0
\end{bmatrix}
$$
(Node 1 connected to 0 and 2).

## 3. Adjacency List

An array of lists. `Adj[i]` contains a list of all vertices connected to vertex $i$.

*   **Space Complexity:** $O(V + E)$
*   **Check Edge:** $O(\text{degree of } V)$
*   **Iterate Neighbors:** $O(\text{degree of } V)$

**Example:**
*   0: [1]
*   1: [0, 2]
*   2: [1]

## 4. Edge List

A simple list of pairs representing edges.
$[(0, 1), (1, 2), (2, 0)]$

*   **Space Complexity:** $O(E)$
*   **Usage:** Kruskal's Algorithm (MST).

## 5. Comparison

| Feature | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Space** | $O(V^2)$ (Heavy) | $O(V+E)$ (Efficient) |
| **Add Edge** | $O(1)$ | $O(1)$ |
| **Check Edge** | $O(1)$ | $O(V)$ (Worst case) |
| **Best For** | Dense Graphs ($E \approx V^2$) | Sparse Graphs ($E \ll V^2$) |

## 6. Implementation Example (Python)

```python
# Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F']
}
```

## 7. Real-World Application in CS

### 1. Social Networks
Facebook (undirected graph) uses adjacency lists because the graph is sparse (average user has ~500 friends, not billions).

### 2. Web Crawlers
Use adjacency lists to store links found on pages to traverse the web.

## 8. Practice Problems

1.  Represent the complete graph $K_4$ using an Adjacency Matrix.
2.  Given a graph with $V=1000$ and $E=5000$, which representation saves more memory?
