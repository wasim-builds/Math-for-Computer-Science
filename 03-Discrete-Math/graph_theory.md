# Graph Theory

## 1. Introduction

A graph is a data structure consisting of **vertices** (nodes) and **edges** (connections).
$$ G = (V, E) $$

## 2. Terminology

*   **Undirected Graph:** Edges have no direction (e.g., Facebook friends).
*   **Directed Graph (Digraph):** Edges have direction (e.g., Twitter followers).
*   **Weighted Graph:** Edges have weights/costs (e.g., Distance between cities).
*   **Cycle:** A path that starts and ends at the same vertex.
*   **Connected Graph:** There is a path between every pair of vertices.
*   **Degree:** Number of edges connected to a vertex.

## 3. Special Graphs

### 1. Trees
A connected graph with no cycles.
*   **Rooted Tree:** One vertex is designated as the root.
*   **Binary Tree:** Each node has at most 2 children.

### 2. Bipartite Graph
Vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to one in the other.

### 3. Complete Graph ($K_n$)
Every pair of distinct vertices is connected by a unique edge.
Total Edges: $\frac{n(n-1)}{2}$

## 4. Graph Algorithms

### 1. BFS (Breadth-First Search)
Explores neighbor nodes first before moving to the next level neighbors (uses Queue).

### 2. DFS (Depth-First Search)
Explores as far as possible along each branch before backtracking (uses Stack/Recursion).

### 3. Dijkstra's Algorithm
Finds the shortest path between nodes in a graph.

## 5. Real-World Application in CS

### 1. Social Networks
Modeling relationships between people.

### 2. Network Routing
Finding the most efficient path for data packets (Internet Protocols).

### 3. Recommendation Systems
Graphs connect users to items they like; algorithms predict new edges (recommendations).

## 6. Solved Examples

**Example 1:**
How many edges in a complete graph with 5 vertices ($K_5$)?

**Solution:**
$$ \frac{5(5-1)}{2} = \frac{20}{2} = 10 $$

**Example 2:**
Does a graph with degrees $\{2, 2, 3, 3, 4\}$ exist?

**Solution:**
Handshaking Lemma: Sum of degrees = $2 \times |E|$.
Sum = $2+2+3+3+4 = 14$. Since 14 is even, such a graph can exist.

## 7. Practice Problems

1.  Draw a graph with 4 vertices and degrees 1, 2, 2, 3.
2.  Find the shortest path using Dijkstra's algorithm (conceptually).
3.  Prove that a tree with $n$ vertices has exactly $n-1$ edges.
