import sympy as sp

def symbolic_limits():
    """
    Demonstrates symbolic limit calculation using SymPy.
    """
    x = sp.symbols('x')
    
    # 1. Basic Limit: limit(x^2 + 3x + 2) as x -> 2
    f1 = x**2 + 3*x + 2
    lim1 = sp.limit(f1, x, 2)
    print(f"Limit of ({f1}) as x -> 2 is: {lim1}")

    # 2. Infinite Limit: limit(1/x) as x -> infinity
    f2 = 1/x
    lim2 = sp.limit(f2, x, sp.oo)
    print(f"Limit of ({f2}) as x -> oo is: {lim2}")

    # 3. Trigonometric Limit: limit(sin(x)/x) as x -> 0 (Squeeze Theorem)
    f3 = sp.sin(x)/x
    lim3 = sp.limit(f3, x, 0)
    print(f"Limit of ({f3}) as x -> 0 is: {lim3}")

    # 4. Exponential Limit: limit((1 + 1/x)^x) as x -> infinity (Definition of e)
    f4 = (1 + 1/x)**x
    lim4 = sp.limit(f4, x, sp.oo)
    print(f"Limit of ({f4}) as x -> oo is: {lim4}")

if __name__ == "__main__":
    print("--- Calculus: Symbolic Limits ---")
    symbolic_limits()
