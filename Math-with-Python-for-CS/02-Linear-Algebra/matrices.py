import numpy as np

def matrix_operations():
    """
    Demonstrates basic matrix operations using NumPy.
    """
    # Define matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    
    # 1. Matrix Multiplication (Dot Product)
    C = np.dot(A, B) # Or A @ B
    print("\nMatrix Multiplication (A @ B):\n", C)
    
    # 2. Transpose
    A_T = A.T
    print("\nTranspose of A:\n", A_T)
    
    # 3. Determinant
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of A: {det_A:.2f}") # 1*4 - 2*3 = -2
    
    # 4. Inverse
    try:
        A_inv = np.linalg.inv(A)
        print("\nInverse of A:\n", A_inv)
        
        # Verify: A @ A_inv should be Identity Matrix
        I = np.dot(A, A_inv)
        print("Verification (A @ A_inv):\n", np.round(I))
    except np.linalg.LinAlgError:
        print("\nMatrix A is singular (no inverse).")

if __name__ == "__main__":
    print("--- Linear Algebra: Matrices ---")
    matrix_operations()
