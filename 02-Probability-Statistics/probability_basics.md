# Probability & Statistics - Basics

## 1. Introduction

Probability is the study of **uncertainty**. It quantifies the likelihood of an event occurring.
$$ 0 \le P(E) \le 1 $$

## 2. Terminology

*   **Experiment:** An action with an uncertain outcome (e.g., tossing a coin).
*   **Sample Space (S):** The set of all possible outcomes.
*   **Event (E):** A subset of the sample space.

## 3. Probability Rules

### 1. Addition Rule (Union)
$$ P(A \cup B) = P(A) + P(B) - P(A \cap B) $$
If A and B are mutually exclusive ($P(A \cap B) = 0$), then:
$$ P(A \cup B) = P(A) + P(B) $$

### 2. Multiplication Rule (Intersection)
$$ P(A \cap B) = P(A) \cdot P(B|A) $$
If A and B are independent:
$$ P(A \cap B) = P(A) \cdot P(B) $$

### 3. Conditional Probability
$$ P(A|B) = \frac{P(A \cap B)}{P(B)} $$
The probability of A occurring given that B has already occurred.

## 4. Random Variables (RV)

A function that maps outcomes of an experiment to numerical values.

*   **Discrete RV:** Takes specific, countable values (e.g., roll of a die).
*   **Continuous RV:** Takes any value within a range (e.g., height, time).

### Expected Value (Mean)
For a discrete random variable X:
$$ E[X] = \sum x \cdot P(X=x) $$
It represents the long-term average outcome.

### Variance using Expectation
$$ Var(X) = E[X^2] - (E[X])^2 $$
It measures the spread of the data.

## 5. Real-World Application in CS

### 1. Machine Learning Classifiers
Naive Bayes classifiers use probability rules to predict outcomes (used in spam filtering).

### 2. Randomized Algorithms
Algorithms like QuickSort use randomness for efficiency.

### 3. Risk Assessment
Calculating the probability of system failure or network congestion.

## 6. Solved Examples

**Example 1:**
A coin is tossed twice. Find the probability of getting at least one Head.

**Solution:**
Sample Space $S = \{HH, HT, TH, TT\}$.
Event $E = \{HH, HT, TH\}$.
$$ P(E) = \frac{3}{4} = 0.75 $$

**Example 2:**
If $P(A) = 0.5$, $P(B) = 0.4$, and $P(A \cap B) = 0.2$, find $P(A \cup B)$.

**Solution:**
$$ P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7 $$

## 7. Practice Problems

1.  A card is drawn from a deck. Find the probability it is a King or a Heart.
2.  Two dice are rolled. Find the probability the sum is 7.
3.  Calculate $E[X]$ for a die roll.
