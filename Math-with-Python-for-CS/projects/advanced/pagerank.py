import numpy as np

def pagerank(M, num_iterations=100, d=0.85):
    """
    M: Adjacency matrix (transition probability matrix)
    d: Damping factor (usually 0.85)
    """
    N = M.shape[1]
    v = np.ones(N) / N  # Initialize rank vector attached to each page
    
    for i in range(num_iterations):
        v = d * M @ v + (1 - d) / N
        
    return v

if __name__ == "__main__":
    # Example: 4 Web Pages (A, B, C, D)
    # A -> B, C
    # B -> C
    # C -> A
    # D -> C
    
    # Transition Logic:
    # If A links to B and C, prob(A->B) = 0.5, prob(A->C) = 0.5
    
    # Column 0 (A): Links to B(1), C(2) -> [0, 0.5, 0.5, 0]
    # Column 1 (B): Links to C(2) -> [0, 0, 1, 0]
    # Column 2 (C): Links to A(0) -> [1, 0, 0, 0]
    # Column 3 (D): Links to C(2) -> [0, 0, 1, 0]
    
    M = np.array([
        [0, 0, 1, 0],   # A
        [0.5, 0, 0, 0], # B
        [0.5, 1, 0, 1], # C
        [0, 0, 0, 0]    # D (Dangel: no outgoing links logic usually handled by teleporting, simplified here)
    ])
    
    final_ranks = pagerank(M)
    print("Page Ranks:")
    pages = ['A', 'B', 'C', 'D']
    for i, rank in enumerate(final_ranks):
        print(f"Page {pages[i]}: {rank:.4f}")
