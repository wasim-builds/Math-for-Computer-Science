# Permutation & Combination Practice Problems

## 1. Basics

1.  A license plate consists of 3 letters followed by 3 numbers. How many possible license plates are there? (Repetition allowed)
2.  How many ways can a president, vice-president, and secretary be chosen from a club of 20 members?
3.  How many ways can a committee of 4 be chosen from 10 men and 8 women, if the committee must have 2 men and 2 women?

## 2. Advanced Counting

1.  How many ways can 6 people be seated around a circular table if two specific people must NOT sit together?
2.  How many distinct permutations of the word "MATHEMATICS"?
3.  Find the number of non-negative integer solutions to $x + y + z + w = 15$.

---

## **Solutions**

### **Basics**
1.  **17,576,000** ($26^3 \times 10^3$)
2.  **6,840** ($P(20, 3) = 20 \times 19 \times 18$)
3.  **1,260** ($C(10, 2) \times C(8, 2) = 45 \times 28$)

### **Advanced Counting**
1.  **72** (Total circular permutations $(6-1)! = 120$. Ways strictly *together* = $(5-1)! \times 2 = 48$. Result = $120 - 48 = 72$)
2.  **4,989,600** ($11! / (2! \times 2! \times 2!)$ -- M, A, T repeated twice each)
3.  **816** ($C(15+4-1, 4-1) = C(18, 3)$)
