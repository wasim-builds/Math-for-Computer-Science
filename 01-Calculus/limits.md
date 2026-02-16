# Calculus - Limits

## 1. Introduction to Limits

A limit asks: *"What value does a function approach as x gets closer and closer to a certain number?"*

It is the foundational block of calculus, defining derivatives and integrals.

**Notation:**
$$ \lim_{x \to c} f(x) = L $$

This reads as: *"The limit of f(x) as x approaches c is L."*

## 2. Types of Limits

### Left-Hand Limit (LHL)
Approaching $c$ from values smaller than $c$:
$$ \lim_{x \to c^-} f(x) $$

### Right-Hand Limit (RHL)
Approaching $c$ from values larger than $c$:
$$ \lim_{x \to c^+} f(x) $$

**Condition for Limit Existence:**
$$ \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L $$

## 3. Properties of Limits

If $\lim_{x \to c} f(x) = A$ and $\lim_{x \to c} g(x) = B$, then:

*   **Sum Rule:** $\lim_{x \to c} [f(x) + g(x)] = A + B$
*   **Difference Rule:** $\lim_{x \to c} [f(x) - g(x)] = A - B$
*   **Product Rule:** $\lim_{x \to c} [f(x) \cdot g(x)] = A \cdot B$
*   **Quotient Rule:** $\lim_{x \to c} \left[\frac{f(x)}{g(x)}\right] = \frac{A}{B}$ (if $B \neq 0$)

## 4. Continuity

A function $f(x)$ is continuous at a point $x = c$ if:
1.  $f(c)$ is defined.
2.  $\lim_{x \to c} f(x)$ exists.
3.  $\lim_{x \to c} f(x) = f(c)$.

**In simpler terms:** You can draw the graph without lifting your pen.

## 5. Real-World Application in CS

### 1. Analysis of Algorithms (Big O Notation)
Limits are used to describe how the runtime of an algorithm grows as the input size $n$ approaches infinity.
$$ O(g(n)) = \{ f(n) : \lim_{n \to \infty} \frac{f(n)}{g(n)} < \infty \} $$

### 2. Machine Learning (Gradient Descent)
The derivative (which is a limit) tells us the slope of the loss function, allowing us to minimize error.

## 6. Solved Examples

**Example 1:**
Evaluate $\lim_{x \to 2} (x^2 + 5)$.

**Solution:**
Since $f(x) = x^2 + 5$ is a polynomial (continuous), direct substitution works:
$$ (2)^2 + 5 = 4 + 5 = 9 $$

**Example 2:**
Evaluate $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$.

**Solution:**
Direct substitution gives $\frac{0}{0}$ (Indeterminate Form). Factorize:
$$ \lim_{x \to 3} \frac{(x-3)(x+3)}{x-3} $$
Cancel $(x-3)$:
$$ \lim_{x \to 3} (x+3) = 3 + 3 = 6 $$

## 7. Practice Problems

1.  Evaluate $\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}$
2.  Evaluate $\lim_{x \to \infty} \frac{3x^2 + 2x - 1}{5x^2 - 4x + 7}$
3.  Find $\lim_{x \to 0} \frac{\sin x}{x}$
