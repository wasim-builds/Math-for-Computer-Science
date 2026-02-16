# Permutations & Combinations - Basics

## 1. Introduction

Combinatorics is the branch of mathematics dealing with counting.

### Fundamental Counting Principle (Multiplication Rule)
If there are $m$ ways to do one thing and $n$ ways to do another, then there are $m \times n$ ways to do both.

## 2. Factorial (!)
The product of all positive integers less than or equal to $n$.
$$ n! = n \times (n-1) \times \dots \times 2 \times 1 $$
*   $0! = 1$
*   $1! = 1$

## 3. Permutations (Order Matters) ($nPr$)
Arranging $r$ items from a set of $n$ distinct items where **order matters**.
$$ P(n, r) = \frac{n!}{(n-r)!} $$

**Example:**
Ways to award Gold, Silver, Bronze medals to 10 runners.
$$ P(10, 3) = \frac{10!}{7!} = 10 \times 9 \times 8 = 720 $$

## 4. Combinations (Order Doesn't Matter) ($nCr$)
Selecting $r$ items from a set of $n$ distinct items where **order does not matter**.
$$ C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!} $$

**Example:**
Ways to choose a committee of 3 people from 10.
$$ C(10, 3) = \frac{10!}{3!7!} = \frac{720}{6} = 120 $$

## 5. Real-World Application in CS

### 1. Password Strength
Calculating the number of possible passwords given a set of characters and length constraints.

### 2. Algorithm Complexity
Analyzing brute-force algorithms (e.g., Travelling Salesman Problem tries all permutations).

### 3. Lottery Odds
Calculating the probability of winning a lottery (choosing 6 numbers out of 49).

## 6. Solved Examples

**Example 1:**
How many ways to arrange the letters "CAT"?

**Solution:**
3 distinct letters. $3! = 3 \times 2 \times 1 = 6$.
(CAT, CTA, ACT, ATC, TCA, TAC).

**Example 2:**
How many handshakes if 5 people meet?

**Solution:**
Order doesn't matter (A implies B is same as B implies A).
$$ C(5, 2) = \frac{5 \times 4}{2 \times 1} = 10 $$

## 7. Practice Problems

1.  Evaluate $P(6, 2)$ and $C(6, 2)$.
2.  How many ways can 5 books be arranged on a shelf?
3.  How many distinct permutations of the word "LEVEL"?
