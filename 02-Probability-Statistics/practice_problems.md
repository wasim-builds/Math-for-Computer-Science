# Probability & Statistics Practice Problems

## 1. Probability Basics

1.  A bag contains 5 red balls and 3 blue balls. Two balls are drawn without replacement. Find the probability that both are red.
2.  If $P(A) = 0.3, P(B) = 0.6$, and A and B are independent, find $P(A \cup B)$.
3.  A fair die is rolled. Let $X$ be the outcome. Find $E[X]$ and $Var(X)$.

## 2. Distributions

1.  (Binomial) A student guesses on a 10-question True/False test. What is the probability they get exactly 8 correct? ($n=10, p=0.5$)
2.  (Poisson) A call center receives an average of 4 calls per minute. What is the probability of receiving 0 calls in a minute?
3.  (Normal) Given $X \sim N(100, 15^2)$, find the $Z$-score for $x=130$.

## 3. Bayes' Theorem

1.  In a certain population, 1% have cancer. A test is 90% accurate for those with cancer (True Positive) and has a 5% false positive rate for those without. If a person tests positive, what is the probability they actually have cancer?
    *   $P(C) = 0.01$
    *   $P(Pos|C) = 0.90$
    *   $P(Pos|\neg C) = 0.05$

---

## **Solutions**

### **Probability Basics**
1.  **5/14** ($\frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$)
2.  **0.72** ($P(A)+P(B)-P(A)P(B) = 0.3+0.6-0.18$)
3.  **$E[X]=3.5, Var(X) \approx 2.92$**

### **Distributions**
1.  **$\approx 0.044$** ($\binom{10}{8} (0.5)^{10}$)
2.  **$\approx 0.018$** ($e^{-4}$)
3.  **2** ($Z = \frac{130-100}{15} = 2$)

### **Bayes' Theorem**
1.  **$\approx 15.38\%$**
    *   $P(Pos) = (0.9)(0.01) + (0.05)(0.99) = 0.009 + 0.0495 = 0.0585$
    *   $P(C|Pos) = \frac{0.009}{0.0585} \approx 0.1538$
