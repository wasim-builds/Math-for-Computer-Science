# Graph Traversal Algorithms

## 1. Breadth-First Search (BFS)

Explores the graph layer by layer. It visits all neighbors of a node before moving to the next level neighbors.

**Data Structure:** Queue (FIFO).

**Algorithm:**
1.  Enqueue starting node.
2.  While queue is not empty:
    *   Dequeue node $u$.
    *   For each neighbor $v$ of $u$:
        *   If $v$ is not visited:
            *   Mark $v$ as visited.
            *   Enqueue $v$.

**PROS:** Finds the shortest path in an unweighted graph.
**Time Complexity:** $O(V + E)$.

## 2. Depth-First Search (DFS)

Explores as far as possible along each branch before backtracking.

**Data Structure:** Stack (LIFO) or Recursion.

**Algorithm:**
1.  Push starting node.
2.  While stack is not empty:
    *   Pop node $u$.
    *   If $u$ is not visited:
        *   Mark $u$ as visited.
        *   For each neighbor $v$ of $u$:
            *   Push $v$.

**PROS:** Uses less memory than BFS. Useful for topological sort, cycle detection.
**Time Complexity:** $O(V + E)$.

## 3. Comparison

| Feature | BFS | DFS |
| :--- | :--- | :--- |
| **Strategy** | Level by Level | Deep Dive |
| **Data Structure** | Queue | Stack / Recursion |
| **Shortest Path?** | Yes (Unweighted) | No |
| **Memory** | High (stores level) | Low (stores path) |

## 4. Real-World Application in CS

### 1. BFS Applications
*   **GPS Navigation:** Finding the shortest route (in unweighted terms) or nearest neighbor.
*   **Social Networks:** Finding people within $k$ degrees of separation.

### 2. DFS Applications
*   **Maze Solving:** Finding *a* path through a maze.
*   **Topological Sorting:** Scheduling tasks with dependencies (e.g., Makefiles, Course Prerequisites).

## 5. Solved Examples

**Example (Pseudo-code):**
Given graph: A -> B, A -> C, B -> D.
**BFS Order:** A, B, C, D.
**DFS Order:** A, B, D, C (or A, C, B, D depending on neighbor order).

## 6. Practice Problems

1.  Perform BFS and DFS on the graph:
    *   0 -> 1, 0 -> 2
    *   1 -> 3, 1 -> 4
    *   2 -> 5, 2 -> 6
2.  Implement BFS in Python to find the shortest path from start to end in a grid.
