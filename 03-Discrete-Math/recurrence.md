# Recurrence Relations

## 1. Introduction

A recurrence relation is an equation that recursively defines a sequence where the next term is a function of the previous terms.

**Example (Fibonacci Sequence):**
$$ F_n = F_{n-1} + F_{n-2} $$
Base cases: $F_0 = 0, F_1 = 1$.

## 2. Solving Recurrence Relations

### 1. Substitution Method
Guess a bound and then prove it using induction.

### 2. Recursion Tree Method
Visualize the recursion as a tree and sum the costs at each level.

### 3. Master Theorem
Provides a direct way to solve recurrences of the form:
$$ T(n) = aT(n/b) + f(n) $$
Where $a \ge 1, b > 1$.

**Cases:**
1.  If $f(n) = O(n^{\log_b a - \epsilon})$, then $T(n) = \Theta(n^{\log_b a})$.
2.  If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$.
3.  If $f(n) = \Omega(n^{\log_b a + \epsilon})$, then $T(n) = \Theta(f(n))$.

## 3. Linear Homogeneous Recurrence Relations

Form: $a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k}$

**Solution Method (Characteristic Equation):**
1.  Assume solution $a_n = r^n$.
2.  Form characteristic equation: $r^k - c_1 r^{k-1} - ... - c_k = 0$.
3.  Find roots $r_1, r_2, ...$.
4.  General solution: $a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + ...$

## 4. Real-World Application in CS

### 1. Analysis of Algorithms
Calculating the time complexity of recursive algorithms like Merge Sort ($T(n) = 2T(n/2) + n$) and Quick Sort.

### 2. Dynamic Programming
Breaking down complex problems into simpler subproblems (e.g., Knapsack problem).

## 5. Solved Examples

**Example 1: Merge Sort**
$$ T(n) = 2T(n/2) + n $$
Here $a=2, b=2, f(n)=n$.
$\log_b a = \log_2 2 = 1$.
Since $f(n) = \Theta(n^1)$, we are in Case 2.
$$ T(n) = \Theta(n \log n) $$

**Example 2: Fibonacci Closed Form**
$F_n = F_{n-1} + F_{n-2}$.
Characteristic Eq: $r^2 - r - 1 = 0$.
Roots: $\frac{1 \pm \sqrt{5}}{2}$ (Golden Ratio $\phi$).
$$ F_n = \frac{1}{\sqrt{5}} (\phi^n - (1-\phi)^n) $$

## 6. Practice Problems

1.  Solve $T(n) = 4T(n/2) + n$. (Use Master Theorem)
2.  Solve $a_n = 5a_{n-1} - 6a_{n-2}$ with $a_0=1, a_1=4$.
3.  Write the recurrence for the Tower of Hanoi problem.
