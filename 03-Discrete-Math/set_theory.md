# Set Theory

## 1. Introduction

A set is a well-defined collection of distinct objects, considered as an object in its own right. Objects in a set are called elements or members.

## 2. Basic Concepts

*   **Roster Method:** $A = \{1, 2, 3, 4, 5\}$
*   **Set-Builder Notation:** $B = \{x \mid x > 0 \text{ and } x \text{ is even}\}$
*   **Empty Set ($\emptyset$):** A set with no elements.
*   **Subset ($A \subseteq B$):** Every element of A is also in B.
*   **Universal Set ($U$):** The set of all objects under consideration.

## 3. Set Operations

Let $A = \{1, 2, 3\}$ and $B = \{3, 4, 5\}$.

### 1. Union ($A \cup B$)
Contains all elements in A or B (or both).
$$ A \cup B = \{1, 2, 3, 4, 5\} $$

### 2. Intersection ($A \cap B$)
Contains only elements present in both A and B.
$$ A \cap B = \{3\} $$

### 3. Difference ($A - B$)
Elements in A but NOT in B.
$$ A - B = \{1, 2\} $$

### 4. Complement ($A^c$ or $A'$)
Elements in the universal set $U$ that are NOT in A.

## 4. Venn Diagrams

Graphical representation of sets and their relationships. Useful for visualizing operations.

## 5. Real-World Application in CS

### 1. Database Operations
SQL `UNION`, `INTERSECT`, and `EXCEPT` operations directly map to set theory.

### 2. Data Structures
`Set` data structures (e.g., `HashSet` in Java, `set` in Python) allow for $O(1)$ lookup and ensure uniqueness of elements.

### 3. Image Processing
Pixels can be treated as sets of points. Operations like erosion and dilation are based on set theory.

## 6. Solved Examples

**Example 1:**
Let $U = \{1, 2, 3, 4, 5\}$, $A=\{1, 2\}$, $B=\{2, 3, 4\}$. Find $(A \cup B)^c$.

**Solution:**
$$ A \cup B = \{1, 2, 3, 4\} $$
$$ (A \cup B)^c = \{5\} $$

**Example 2:**
Prove that $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ (Distributive Law).
*(Proof typically done using element chasing or truth tables)*

## 7. Practice Problems

1.  Given $A=\{x, y, z\}$ and $B=\{y, z, w\}$, find $A \oplus B$ (Symmetric Difference).
2.  If $|A|=10, |B|=20, |A \cap B|=5$, find $|A \cup B|$ using Inclusion-Exclusion Principle.
3.  Write the power set of $S = \{a, b\}$.
