def fibonacci_iterative(n):
    """
    Solves F(n) = F(n-1) + F(n-2) iteratively.
    Time Complexity: O(n)
    """
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n, memo={}):
    """
    Solves F(n) using recursion with memoization.
    Time Complexity: O(n)
    """
    if n in memo: return memo[n]
    if n <= 1: return n
    
    memo[n] = fibonacci_recursive(n-1, memo) + fibonacci_recursive(n-2, memo)
    return memo[n]

def solve_recurrence(c1, c2, a0, a1, n):
    """
    Solves linear homogeneous recurrence: a_n = c1*a_{n-1} + c2*a_{n-2}
    """
    # Simply using iteration for demonstration
    seq = [a0, a1]
    for i in range(2, n+1):
        next_val = c1 * seq[i-1] + c2 * seq[i-2]
        seq.append(next_val)
    return seq

if __name__ == "__main__":
    print("--- Discrete Math: Recurrence Relations ---")
    
    n = 10
    print(f"Fibonacci({n}) Iterative: {fibonacci_iterative(n)}")
    print(f"Fibonacci({n}) Recursive: {fibonacci_recursive(n)}")
    
    # Example: a_n = 5*a_{n-1} - 6*a_{n-2} (Roots 2, 3)
    # Sequence: 1, 4, 14, 46...
    seq = solve_recurrence(5, -6, 1, 4, 6)
    print(f"\nRecurrence a_n = 5a_{n-1} - 6a_{n-2}: {seq}")
