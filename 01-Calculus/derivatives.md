# Calculus - Derivatives

## 1. Definition of Derivative

The derivative measures the **instantaneous rate of change** of a function with respect to a variable.

**Geometric Interpretation:** The slope of the tangent line to the curve at a point.

**Formal Definition (First Principles):**
$$ f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} $$

## 2. Common Derivative Rules

### Power Rule
$$ \frac{d}{dx}(x^n) = nx^{n-1} $$

### Product Rule
$$ (uv)' = u'v + uv' $$

### Quotient Rule
$$ \left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2} $$

### Chain Rule
$$ \frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x) $$

## 3. Partial Derivatives

For multivariable functions $f(x, y)$, we differentiate with respect to one variable while treating the others as constants.

**Notation:**
$$ \frac{\partial f}{\partial x} $$

**Example:**
If $f(x, y) = x^2y + 3x$, then:
$$ \frac{\partial f}{\partial x} = 2xy + 3 $$
$$ \frac{\partial f}{\partial y} = x^2 $$

## 4. The Gradient Vector ($\nabla$)

The gradient is a vector containing all partial derivatives. It points in the direction of the steepest ascent.

$$ \nabla f = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix} $$

**Application:** Used in Gradient Descent to minimize loss functions in Machine Learning.

## 5. Real-World Application in CS

### 1. Neural Networks (Backpropagation)
Derivatives are used to calculate gradients of the loss function with respect to weights, allowing the network to "learn."

### 2. Optimization
Finding the minimum or maximum of a function (e.g., minimizing cost, maximizing efficiency). Set $f'(x) = 0$ to find critical points.

## 6. Solved Examples

**Example 1:**
Find the derivative of $f(x) = 3x^4 - 2x^2 + 5$.

**Solution:**
Using the Power Rule:
$$ f'(x) = 12x^3 - 4x $$

**Example 2:**
Find the partial derivatives of $f(x, y) = x^3 + y^2 - 4xy$.

**Solution:**
$$ \frac{\partial f}{\partial x} = 3x^2 - 4y $$
$$ \frac{\partial f}{\partial y} = 2y - 4x $$

## 7. Practice Problems

1.  Differentiate $y = \sin(x^2)$
2.  Find the gradient of $f(x, y) = x^2 + y^2$ at point (1, 2)
3.  Find critical points for $f(x) = x^3 - 3x$
