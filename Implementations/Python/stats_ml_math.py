import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. Normal Distribution Visualization
def plot_normal_distribution(mu, sigma):
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma))
    plt.title(f"Normal Distribution (mu={mu}, sigma={sigma})")
    plt.xlabel("Value")
    plt.ylabel("Probability Density")
    plt.show()

print("Plotting Normal Distribution...")
plot_normal_distribution(0, 1)

# 2. Matrix Operations (Linear Algebra)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

# Dot Product
C = np.dot(A, B)
print("\nDot Product (A . B):\n", C)

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

# 3. Probability Simulation (Coin Toss)
def simulate_coin_toss(n_trials):
    results = np.random.randint(0, 2, n_trials) # 0 for Tails, 1 for Heads
    heads_count = np.sum(results)
    prob_heads = heads_count / n_trials
    print(f"\nSimulated {n_trials} coin tosses.")
    print(f"Heads: {heads_count}, Probability: {prob_heads}")

simulate_coin_toss(1000)

# 4. Gradient Descent (Optimization)
def gradient_descent(start_x, learning_rate, n_iters):
    # Function: f(x) = x^2, Derivative: f'(x) = 2x
    x = start_x
    history = []
    
    for _ in range(n_iters):
        gradient = 2 * x
        x = x - learning_rate * gradient
        history.append(x)
        
    return x, history

final_x, history = gradient_descent(start_x=10, learning_rate=0.1, n_iters=20)
print(f"\nGradient Descent found minimum at x = {final_x:.4f} (Expected: 0)")
