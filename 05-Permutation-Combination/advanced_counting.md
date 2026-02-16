# Permutations & Combinations - Advanced Counting

## 1. Circular Permutations

Number of ways to arrange $n$ distinct objects in a circle.
$$ P_{circle} = (n-1)! $$

**Why?** Because rotating the circle doesn't change the relative order.

## 2. Permutations with Repetition

Number of distinct permutations of $n$ objects where there are $n_1$ indistinguishable items of type 1, $n_2$ of type 2, etc.
$$ P = \frac{n!}{n_1! n_2! \dots n_k!} $$

**Example:**
Arranging letters in "MISSISSIPPI".
Total letters ($n=11$). 4 'S', 4 'I', 2 'P'.
$$ \frac{11!}{4! 4! 2!} $$

## 3. Stars and Bars (Balls and Bins)

Number of ways to distribute $n$ identical items into $k$ distinct bins.
$$ C(n+k-1, n) \text{ or } C(n+k-1, k-1) $$

**Example:**
How many ways to distribute 10 identical candies among 3 children?
$n=10, k=3$.
$$ \binom{10+3-1}{10} = \binom{12}{10} = \binom{12}{2} = 66 $$

## 4. Inclusion-Exclusion Principle

For two sets: $|A \cup B| = |A| + |B| - |A \cap B|$

For three sets: $|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$

**Application:** Counting derangements (permutations where no element appears in its original position).

## 5. Pigeonhole Principle

If $n$ items are put into $m$ containers, with $n > m$, then at least one container must contain more than one item.

**CS Application:**
Hashing collisions. If you have more keys than hash buckets, collisions are inevitable.

## 6. Solved Examples

**Example 1:**
How many non-negative integer solutions to $x_1 + x_2 + x_3 = 10$?

**Solution:**
This is a Stars and Bars problem. $n=10, k=3$.
$$ \binom{10+3-1}{2} = \binom{12}{2} = 66 $$

**Example 2:**
In a group of 13 people, must two have their birthday in the same month?

**Solution:**
Pigeonholes ($m$) = 12 months. Pigeons ($n$) = 13 people.
Since $13 > 12$, yes, at least two must share a birth month.

## 7. Practice Problems

1.  How many ways to arrange 5 people around a round table?
2.  How many distinct permutations of the word "BANANA"?
3.  Show that in any group of 6 people, there are either 3 mutual friends or 3 mutual strangers (Ramsey Theory).
