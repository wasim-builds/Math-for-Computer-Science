import math
import itertools

def permutations_combinations():
    """
    Demonstrates Permutations and Combinations using math and itertools.
    """
    n = 5
    r = 3
    
    print(f"n = {n}, r = {r}")
    
    # 1. Factorial
    fact_n = math.factorial(n)
    print(f"Factorial ({n}!): {fact_n}")
    
    # 2. Permutations (nPr) - Order Matters
    # Formula: n! / (n-r)!
    nPr = math.perm(n, r)
    print(f"Permutations P({n}, {r}): {nPr}")
    
    # List actual permutations using itertools
    items = ['A', 'B', 'C', 'D', 'E']
    perms = list(itertools.permutations(items[:n], r))
    print(f"First 5 Permutations of {items[:n]} choose {r}: {perms[:5]}...")
    
    # 3. Combinations (nCr) - Order Doesn't Matter
    # Formula: n! / (r! * (n-r)!)
    nCr = math.comb(n, r)
    print(f"Combinations C({n}, {r}): {nCr}")
    
    # List actual combinations using itertools
    combs = list(itertools.combinations(items[:n], r))
    print(f"All Combinations of {items[:n]} choose {r}: {combs}")

if __name__ == "__main__":
    print("--- Discrete Math: Counting ---")
    permutations_combinations()
