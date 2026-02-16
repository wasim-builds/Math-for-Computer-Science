import numpy as np
import matplotlib.pyplot as plt

def gradient_descent_1d(start_x, learning_rate, n_iters):
    """
    Performs Gradient Descent to minimize f(x) = x^2.
    Derivative f'(x) = 2x.
    """
    x = start_x
    history = [x]
    
    for _ in range(n_iters):
        gradient = 2 * x
        x = x - learning_rate * gradient
        history.append(x)
        
    return x, history

def plot_gradient_descent(history):
    """
    Visualizes the path taken by Gradient Descent.
    """
    x = np.linspace(-12, 12, 100)
    y = x**2
    
    history = np.array(history)
    history_y = history**2
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x) = x^2')
    plt.scatter(history, history_y, color='red', label='GD Steps', zorder=5)
    plt.plot(history, history_y, color='red', linestyle='--', alpha=0.5)
    
    plt.title("Gradient Descent Optimization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    start_x = 10
    lr = 0.1
    iters = 20
    
    print(f"Starting Gradient Descent at x={start_x}, lr={lr}, iterations={iters}")
    min_x, hist = gradient_descent_1d(start_x, lr, iters)
    
    print(f"Minimum found at: {min_x:.4f}")
    print(f"Actual minimum: 0.0")
    
    # Uncomment to visualize
    # plot_gradient_descent(hist)
