# Time Complexity Math for Interviews

## 1. Big O Notation

Describes the **upper bound** of an algorithm's growth rate. It answers: *"What is the worst-case scenario?"*

*   **Definition:** $f(n) = O(g(n))$ if there exist constants $c, n_0$ such that $0 \le f(n) \le c \cdot g(n)$ for all $n \ge n_0$.

## 2. Common Complexities

| Notation | Name | Example Algorithm |
| :--- | :--- | :--- |
| $O(1)$ | Constant | Accessing array index |
| $O(\log n)$ | Logarithmic | Binary Search |
| $O(n)$ | Linear | Linear Search |
| $O(n \log n)$ | Linearithmic | Merge Sort, Heap Sort |
| $O(n^2)$ | Quadratic | Bubble Sort |
| $O(2^n)$ | Exponential | Recursive Fibonacci |
| $O(n!)$ | Factorial | Permutations |

## 3. How to Calculate Complexity?

1.  **Loops:** A loop running $N$ times $\rightarrow O(N)$.
2.  **Nested Loops:** Loop inside a loop $\rightarrow O(N^2)$.
3.  **Halving:** Loop where $i$ is divided by 2 each step $\rightarrow O(\log N)$.
4.  **Recursion:** Count the number of recursive calls $\times$ work per call.

## 4. Logarithms in CS

Why is $\log_2 n$ so common?
Because many algorithms (divide and conquer) split the input in half at each step.
$$ 2^x = n \Rightarrow x = \log_2 n $$
**Example:** Binary Search.
Given 1000 items, you find target in $\approx 10$ steps ($2^{10} = 1024$).
Given 1,000,000 items, you find target in $\approx 20$ steps ($2^{20} \approx 10^6$).

## 5. Amortized Analysis

Average time per operation over a sequence of operations.
**Example:** Resizing a Dynamic Array (ArrayList/Vector).
Most inserts are $O(1)$. When full, it doubles size ($O(N)$).
Amortized complexity is still $O(1)$.

## 6. Interview Questions

**Q1: What is the complexity of this code?**
```python
for i in range(n):
    j = 1
    while j < n:
        print(j)
        j *= 2
```
**Answer:** The outer loop runs $N$ times. The inner loop runs $\log N$ times. Total: $O(N \log N)$.

**Q2: Complexity of finding a duplicate in an array?**
*   Brute Force: $O(N^2)$
*   Sort first: $O(N \log N)$
*   HashSet: $O(N)$ Space $O(N)$
