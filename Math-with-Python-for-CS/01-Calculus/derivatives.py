import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def symbolic_derivatives():
    """
    Demonstrates symbolic differentiation using SymPy.
    """
    x = sp.symbols('x')
    
    # 1. Polynomial: x^3 - 4x^2 + 5
    f = x**3 - 4*x**2 + 5
    df = sp.diff(f, x)
    print(f"Function: {f}")
    print(f"Derivative: {df}")

    # 2. Trigonometric: sin(x) * cos(x)
    g = sp.sin(x) * sp.cos(x)
    dg = sp.diff(g, x)
    print(f"\nFunction: {g}")
    print(f"Derivative: {dg}") # Expected: cos^2(x) - sin^2(x) = cos(2x)

def numerical_derivative(f, x, h=1e-5):
    """
    Approximates the derivative using the limit definition.
    f'(x) approx (f(x+h) - f(x)) / h
    """
    return (f(x + h) - f(x)) / h

def plot_derivative():
    """
    Visualizes function and its derivative.
    """
    x = np.linspace(-5, 5, 100)
    f = lambda x: x**2
    df_exact = lambda x: 2*x
    df_approx = numerical_derivative(f, x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, f(x), label='f(x) = x^2')
    plt.plot(x, df_exact(x), label="f'(x) Exact (2x)", linestyle='--')
    plt.plot(x, df_approx, label="f'(x) Numerical", linestyle=':', alpha=0.7)
    plt.legend()
    plt.title("Function vs Derivative")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    print("--- Calculus: Derivatives ---")
    symbolic_derivatives()
    # Uncomment to plot
    # plot_derivative()
