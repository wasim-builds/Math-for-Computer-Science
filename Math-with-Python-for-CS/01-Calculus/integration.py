import sympy as sp
import numpy as np
from scipy.integrate import quad

def symbolic_integration():
    """
    Demonstrates symbolic integration using SymPy.
    """
    x = sp.symbols('x')
    
    # 1. Indefinite Integral: integral(x^2) dx
    f1 = x**2
    F1 = sp.integrate(f1, x)
    print(f"Indefinite Integral of {f1}: {F1} + C")

    # 2. Definite Integral: integral(sin(x)) from 0 to pi
    f2 = sp.sin(x)
    F2 = sp.integrate(f2, (x, 0, sp.pi))
    print(f"Definite Integral of {f2} from 0 to pi: {F2}")

def numerical_integration():
    """
    Demonstrates numerical integration using SciPy.
    """
    # 1. Integral of e^(-x^2) from -inf to inf (Gaussian Integral)
    f = lambda x: np.exp(-x**2)
    result, error = quad(f, -np.inf, np.inf)
    print(f"Numerical Integral of e^(-x^2) from -inf to inf: {result:.5f} (Error: {error:.2e})")

if __name__ == "__main__":
    print("--- Calculus: Integration ---")
    symbolic_integration()
    print("\n--- Numerical Integration ---")
    numerical_integration()
