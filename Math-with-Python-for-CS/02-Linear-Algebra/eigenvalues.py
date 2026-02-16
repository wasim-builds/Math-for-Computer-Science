import numpy as np
import matplotlib.pyplot as plt

def eigen_decomposition():
    """
    Visualizes Eigenvalues and Eigenvectors.
    """
    A = np.array([[2, 0], [0, 3]]) # Diagonal matrix for simplicity
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    print("Matrix A:\n", A)
    print("\nEigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
    
    # Visualization
    origin = [0, 0]
    
    # Original vectors (basis)
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    
    # Transformed vectors
    t1 = np.dot(A, v1)
    t2 = np.dot(A, v2)
    
    plt.figure(figsize=(6, 6))
    
    # Plot eigenvectors
    for i in range(len(eigenvalues)):
        vec = eigenvectors[:, i]
        val = eigenvalues[i]
        plt.quiver(*origin, *vec, color=['r', 'b'][i], scale=1, scale_units='xy', label=f'Eigenvector {i+1} (lambda={val})')
        
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.grid()
    plt.title("Eigenvectors Visualization")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("--- Linear Algebra: Eigenvalues ---")
    eigen_decomposition()
