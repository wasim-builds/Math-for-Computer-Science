import numpy as np
import matplotlib.pyplot as plt

def estimate_pi_monte_carlo(n_points):
    """
    Estimates the value of Pi using Monte Carlo simulation.
    Area of circle = pi * r^2
    Area of square = (2r)^2 = 4r^2
    Ratio = pi/4
    """
    # Generate random points in square [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_points)
    y = np.random.uniform(-1, 1, n_points)
    
    # Distance from origin
    dist = x**2 + y**2
    inside_circle = dist <= 1
    
    pi_estimate = 4 * np.sum(inside_circle) / n_points
    
    print(f"Monte Carlo Estimation of Pi ({n_points} points): {pi_estimate:.5f}")
    
    # Visualization
    plt.figure(figsize=(6, 6))
    plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label='Inside')
    plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Outside')
    plt.title(f"Monte Carlo Pi Estimation (Pi approx {pi_estimate:.4f})")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("--- Probability: Simulations ---")
    # small number for quick demo, increase for better accuracy
    estimate_pi_monte_carlo(5000) 
