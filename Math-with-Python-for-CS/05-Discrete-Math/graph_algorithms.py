from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # Undirected

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        print(f"BFS starting from {start_node}:", end=" ")
        
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
            print(f"DFS starting from {start_node}:", end=" ")
        
        visited.add(start_node)
        print(start_node, end=" ")
        
        for neighbor in self.adj_list.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

def visualize_graph():
    G = nx.Graph()
    G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')])
    
    plt.figure(figsize=(6, 4))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_weight='bold')
    plt.title("Graph Visualization")
    plt.show()

if __name__ == "__main__":
    print("--- Discrete Math: Graph Algorithms ---")
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    
    g.bfs('A')
    g.dfs('A')
    print()
    
    # Uncomment to visualize
    # visualize_graph()
