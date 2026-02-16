# Bayes' Theorem

## 1. Introduction

Bayes' Theorem describes the probability of an event based on prior knowledge of conditions that might be related to the event.

It is the mathematical formula for updating beliefs given new evidence.

**Formula:**
$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$

Where:
*   $P(A|B)$: Posterior Probability (Probability of A given B is true).
*   $P(B|A)$: Likelihood (Probability of B given A is true).
*   $P(A)$: Prior Probability (Initial probability of A).
*   $P(B)$: Marginal Probability (Total probability of B).

## 2. Derivation

From the definition of conditional probability:
$$ P(A \cap B) = P(A|B)P(B) $$
$$ P(A \cap B) = P(B|A)P(A) $$

Equating both sides:
$$ P(A|B)P(B) = P(B|A)P(A) $$
$$ \Rightarrow P(A|B) = \frac{P(B|A)P(A)}{P(B)} $$

## 3. Law of Total Probability

Used to calculate the denominator $P(B)$ when B can occur via multiple mutually exclusive paths $A_1, A_2, ..., A_n$.

$$ P(B) = \sum P(B|A_i)P(A_i) $$

## 4. Real-World Application in CS

### 1. Spam Filters
Given the probability that a message contains the word "Free" given it is spam ($P(\text{Free}|\text{Spam})$), we can calculate the probability it is spam given it contains "Free" ($P(\text{Spam}|\text{Free})$).

### 2. Medical Diagnosis
Calculating the probability of a disease given a positive test result, considering the test's false positive rate and the disease's prevalence.

### 3. Machine Learning
Maximum A Posteriori (MAP) estimation uses Bayes' Theorem to estimate parameters.

## 5. Solved Examples

**Example 1: Medical Test**
*   Disease Rate $P(D) = 0.01$ (1% of pop has disease).
*   Test Accuracy $P(Pos|D) = 0.99$ (True Positive).
*   False Positive Rate $P(Pos|\neg D) = 0.05$.
*   A patient tests positive. What is the probability they have the disease?

**Solution:**
$$ P(D|Pos) = \frac{P(Pos|D)P(D)}{P(Pos)} $$
Calculate $P(Pos)$ using Total Probability:
$$ P(Pos) = P(Pos|D)P(D) + P(Pos|\neg D)P(\neg D) $$
$$ P(Pos) = (0.99 \times 0.01) + (0.05 \times 0.99) = 0.0099 + 0.0495 = 0.0594 $$
Now, calculate Posterior:
$$ P(D|Pos) = \frac{0.0099}{0.0594} \approx 0.166 $$
**Result:** Even with a positive test, there is only a 16.6% chance of having the disease!

## 6. Practice Problems

1.  Given $P(A) = 0.4, P(B|A) = 0.8, P(B|\neg A) = 0.1$, find $P(A|B)$.
2.  A factory has two machines. Machine A produces 60% of items (1% defective). Machine B produces 40% (2% defective). If an item is defective, what is the probability it came from Machine A?
