import numpy as np

def numpy_essentials():
    """
    Essential NumPy functions for Data Science and ML.
    """
    # 1. Array Creation
    arr = np.array([1, 2, 3, 4, 5])
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    eye = np.eye(3) # Identity matrix
    rand = np.random.rand(2, 2)
    
    print("Array:", arr)
    print("Zeros:\n", zeros)
    
    # 2. Reshaping
    reshaped = np.arange(9).reshape(3, 3)
    print("\nReshaped (3x3):\n", reshaped)
    
    # 3. Slicing
    print("\nSlice [0:2, 1]:", reshaped[0:2, 1])
    
    # 4. Mathematical Operations
    print("\nSum:", np.sum(arr))
    print("Mean:", np.mean(arr))
    print("Max:", np.max(arr))
    print("Argmax (index of max):", np.argmax(arr))
    
    # 5. Broadcasting
    # Adding a scalar to a vector
    broadcasted = arr + 10
    print("\nBroadcasting (arr + 10):", broadcasted)

if __name__ == "__main__":
    print("--- Linear Algebra: NumPy Basics ---")
    numpy_essentials()
