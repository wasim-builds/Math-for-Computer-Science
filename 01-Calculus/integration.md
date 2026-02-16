# Calculus - Integration

## 1. Concept of Integration

Integration is the reverse process of differentiation. It is used to find the area under a curve.

**Indefinite Integral (Antiderivative):**
$$ \int f(x) dx = F(x) + C $$
Where $C$ is the constant of integration.

**Definite Integral:**
$$ \int_{a}^{b} f(x) dx = F(b) - F(a) $$
This computes the net area between the curve $f(x)$ and the x-axis from $x = a$ to $x = b$.

## 2. Common Integration Rules

### Power Rule
$$ \int x^n dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1) $$

### Exponential Rule
$$ \int e^x dx = e^x + C $$

### Logarithmic Rule
$$ \int \frac{1}{x} dx = \ln|x| + C $$

## 3. Techniques of Integration

### 1. U-Substitution
Used when the integrand is a composite function.
Let $u = g(x)$, then substitute $du = g'(x)dx$.

### 2. Integration by Parts
Based on the Product Rule for differentiation.
$$ \int u dv = uv - \int v du $$
Choose $u$ according to LIATE (Logarithmic, Inverse Trig, Algebraic, Trig, Exponential).

## 4. Real-World Application in CS

### 1. Probability
In continuous probability distributions, the probability that a variable $X$ falls between $a$ and $b$ is the integral of the Probability Density Function (PDF):
$$ P(a \le X \le b) = \int_{a}^{b} f(x) dx $$

### 2. Signal Processing
Fourier Transforms use integrals to decompose signals into frequencies.

### 3. Physics Engines
Used to compute position from velocity ($v = \int a dt$) and velocity from acceleration.

## 5. Solved Examples

**Example 1:**
Evaluate $\int (3x^2 + 4x - 5) dx$.

**Solution:**
$$ x^3 + 2x^2 - 5x + C $$

**Example 2:**
Evaluate $\int_{1}^{2} 2x dx$.

**Solution:**
Antiderivative is $x^2$.
Apply limits: $F(2) - F(1) = 2^2 - 1^2 = 4 - 1 = 3$.

## 6. Practice Problems

1.  Evaluate $\int x \cos(x^2) dx$
2.  Find area under $y = x^2$ from $x=0$ to $x=3$
3.  Compute $\int e^{2x} dx$
