import numpy as np

def vector_operations():
    """
    Demonstrates basic vector operations using NumPy.
    """
    # Define vectors
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    
    print(f"Vector v1: {v1}")
    print(f"Vector v2: {v2}")
    
    # 1. Addition
    v_sum = v1 + v2
    print(f"Addition (v1 + v2): {v_sum}")
    
    # 2. Scalar Multiplication
    v_scaled = 3 * v1
    print(f"Scalar Multiplication (3 * v1): {v_scaled}")
    
    # 3. Dot Product
    dot_prod = np.dot(v1, v2)
    print(f"Dot Product (v1 . v2): {dot_prod}") # 1*4 + 2*5 + 3*6 = 4+10+18 = 32
    
    # 4. Norm (Magnitude)
    norm_v1 = np.linalg.norm(v1)
    print(f"Norm (Magnitude) of v1: {norm_v1:.4f}") # sqrt(1+4+9) = sqrt(14)
    
    # 5. Cosine Similarity
    cos_sim = dot_prod / (np.linalg.norm(v1) * np.linalg.norm(v2))
    print(f"Cosine Similarity: {cos_sim:.4f}")

if __name__ == "__main__":
    print("--- Linear Algebra: Vectors ---")
    vector_operations()
