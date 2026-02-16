import matplotlib.pyplot as plt
import numpy as np

def visualize_data():
    """
    Demonstrates common data visualizations.
    """
    n_points = 100
    
    # 1. Histogram (Frequency Distribution)
    data = np.random.normal(0, 1, 1000)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')
    plt.title("Histogram (Normal Dist)")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    
    # 2. Scatter Plot (Relationship between variables)
    x = np.random.rand(n_points)
    y = 2 * x + np.random.normal(0, 0.1, n_points) # Linear correlation + noise
    
    plt.subplot(1, 2, 2)
    plt.scatter(x, y, color='purple', alpha=0.6)
    plt.title("Scatter Plot (Correlation)")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("--- Statistics: Data Visualization ---")
    visualize_data()
