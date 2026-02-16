# Discrete Math - Logic

## 1. Introduction

Logic is the foundation of mathematical reasoning and computer programming. It deals with statements that are either **True** or **False**.

## 2. Propisitional Logic

A **proposition** is a declarative statement that is either true or false.

### Basic Operators

| Operator | Symbol | Meaning | Example |
| :--- | :---: | :--- | :--- |
| Negation | $\neg p$ | Not $p$ | "It is not raining" |
| Conjunction | $p \land q$ | $p$ AND $q$ | "It is raining AND cold" |
| Disjunction | $p \lor q$ | $p$ OR $q$ | "It is raining OR cold" |
| Exclusive OR | $p \oplus q$ | $p$ XOR $q$ | "Either p or q, but not both" |
| Implication | $p \rightarrow q$ | If $p$ then $q$ | "If it rains, ground is wet" |
| Biconditional | $p \leftrightarrow q$ | $p$ if and only if $q$ | "$p$ is true iff $q$ is true" |

## 3. Truth Tables

**Conjunction ($p \land q$):** True only if both are true.
**Disjunction ($p \lor q$):** True if at least one is true.
**Implication ($p \rightarrow q$):** False only if $p$ is True and $q$ is False.

## 4. Predicate Logic

Extends propositional logic with quantifiers.

### Quantifiers
*   **Universal Quantifier ($\forall$):** "For all".
    *   $\forall x P(x)$: "P(x) is true for all x".
*   **Existential Quantifier ($\exists$):** "There exists".
    *   $\exists x P(x)$: "There is at least one x such that P(x) is true".

## 5. Real-World Application in CS

### 1. Circuit Design
Logic gates (AND, OR, NOT) are the physical implementation of boolean logic.

### 2. Database Queries
SQL queries use logic to filter data (e.g., `WHERE age > 18 AND status = 'active'`).

### 3. Artificial Intelligence
Knowledge representation and reasoning systems use first-order logic to infer new knowledge.

## 6. Solved Examples

**Example 1:**
Construct the truth table for $\neg (p \land q)$.

**Solution:**
| p | q | $p \land q$ | $\neg (p \land q)$ |
| :---: | :---: | :---: | :---: |
| T | T | T | F |
| T | F | F | T |
| F | T | F | T |
| F | F | F | T |
*(This is equivalent to $\neg p \lor \neg q$ by De Morgan's Law)*

**Example 2:**
Translate to logic: "Every student in this class has taken a course in Java."
*   $S(x)$: x is a student in this class.
*   $J(x)$: x has taken Java.

**Solution:**
$$ \forall x (S(x) \rightarrow J(x)) $$

## 7. Practice Problems

1.  Construct the truth table for $(p \rightarrow q) \land (q \rightarrow r)$.
2.  Use De Morgan's Laws to negate: "It is raining and not cold".
3.  Translate: "There exists a number that is prime and even".
