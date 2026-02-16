# The Master Theorem for Divide & Conquer

## 1. Introduction

The Master Theorem provides an easy way to solve recurrence relations of the form:

$$ T(n) = aT\left(\frac{n}{b}\right) + f(n) $$

Where:
*   $n$ = Size of the problem.
*   $a \ge 1$ = Number of subproblems in the recursion.
*   $n/b$ = Size of each subproblem ($b > 1$).
*   $f(n)$ = Cost of the work done outside the recursive calls (e.g., merging or partitioning).

## 2. Comparison

We compare $f(n)$ with $n^{\log_b a}$ (the "critical exponent").

Let $c_{crit} = \log_b a$.

### Case 1: Work at Leaves Dominates
If $f(n) = O(n^{c_{crit} - \epsilon})$ for some $\epsilon > 0$, then:
$$ T(n) = \Theta(n^{\log_b a}) $$
*(Recursion tree is heavy at the bottom)*.

### Case 2: Work is Evenly Distributed
If $f(n) = \Theta(n^{c_{crit}} \log^k n)$ for some $k \ge 0$, then:
$$ T(n) = \Theta(n^{\log_b a} \log^{k+1} n) $$
*(Each level of recursion tree does same work)*.

### Case 3: Work at Root Dominates
If $f(n) = \Omega(n^{c_{crit} + \epsilon})$ for some $\epsilon > 0$, AND regularity condition holds ($a f(n/b) \le c f(n)$), then:
$$ T(n) = \Theta(f(n)) $$
*(Root does most of the work)*.

## 3. Algorithm Examples

### 1. Binary Search
$$ T(n) = T(n/2) + O(1) $$
*   $a=1, b=2, f(n)=1$.
*   $\log_2 1 = 0$.
*   $f(n) = n^0 = 1$. This is Case 2 ($k=0$).
*   **Result:** $T(n) = \Theta(n^0 \log n) = \Theta(\log n)$.

### 2. Merge Sort
$$ T(n) = 2T(n/2) + O(n) $$
*   $a=2, b=2, f(n)=n$.
*   $\log_2 2 = 1$.
*   $f(n) = n^1$. This is Case 2 ($k=0$).
*   **Result:** $T(n) = \Theta(n^1 \log n) = \Theta(n \log n)$.

### 3. Strassen's Matrix Multiplication
$$ T(n) = 7T(n/2) + O(n^2) $$
*   $a=7, b=2, f(n)=n^2$.
*   $\log_2 7 \approx 2.81$.
*   $f(n) = n^2$. Since $2 < 2.81$, $f(n)$ grows slower. Case 1.
*   **Result:** $T(n) = \Theta(n^{\log_2 7}) \approx O(n^{2.81})$.

## 4. Practice Problems

1.  Solve $T(n) = 4T(n/2) + n$.
2.  Solve $T(n) = 4T(n/2) + n^2$.
3.  Solve $T(n) = 4T(n/2) + n^3$.
