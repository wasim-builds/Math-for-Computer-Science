# Probability Distributions

## 1. Introduction

A probability distribution describes how probabilities are distributed over the values of a random variable.

## 2. Discrete Distributions

### 1. Bernoulli Distribution
Describes a single trial with two outcomes: Success (1) or Failure (0).
*   **PMF:** $P(X=k) = p^k(1-p)^{1-k}$ for $k \in \{0, 1\}$
*   **Mean:** $p$
*   **Variance:** $p(1-p)$

### 2. Binomial Distribution
Describes the number of successes in $n$ independent Bernoulli trials.
*   **PMF:** $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
*   **Mean:** $np$
*   **Variance:** $np(1-p)$

### 3. Poisson Distribution
Models the number of events occurring in a fixed interval of time or space.
*   **PMF:** $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$
*   **Mean:** $\lambda$
*   **Variance:** $\lambda$

## 3. Continuous Distributions

### 1. Uniform Distribution
All outcomes in the range $[a, b]$ are equally likely.
*   **PDF:** $f(x) = \frac{1}{b-a}$ for $a \le x \le b$

### 2. Normal (Gaussian) Distribution
The most important distribution in statistics due to the Central Limit Theorem.
Bell-shaped curve defined by mean $\mu$ and variance $\sigma^2$.
*   **PDF:** $f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
*   **Standard Normal Distribution:** $\mu = 0, \sigma = 1$ (Z-score).

### 3. Exponential Distribution
Models the time between events in a Poisson process.
*   **PDF:** $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$
*   **Mean:** $1/\lambda$

## 4. Real-World Application in CS

### 1. A/B Testing
Binomial distribution is used to model click-through rates (CTR) and determine if a new feature is better.

### 2. Queueing Theory
Poisson distribution models arrival of requests at a server. Exponential distribution models service times.

### 3. Anomaly Detection
Data points that fall far from the mean in a Normal distribution (e.g., > 3$\sigma$) are flagged as outliers/anomalies.

## 5. Solved Examples

**Example 1:**
A coin is tossed 10 times. Find probability of exactly 5 Heads.
Given $n=10, p=0.5$.

**Solution:**
$$ P(X=5) = \binom{10}{5} (0.5)^5 (0.5)^5 \approx 0.246 $$

**Example 2:**
Requests arrive at a server at a rate of $\lambda = 5$ per minute. Find prob of exactly 3 requests in a minute.

**Solution:**
$$ P(X=3) = \frac{5^3 e^{-5}}{3!} \approx \frac{125 \times 0.0067}{6} \approx 0.14 $$

## 6. Practice Problems

1.  Find the probability of getting 2 successes in 5 trials with $p=0.3$.
2.  Calculate probabilities for a Poisson process with $\lambda = 2$.
3.  Standardize a value $x=50$ given $\mu=40, \sigma=5$.
