# Matrices

## 1. Introduction

A matrix is a 2-dimensional array of numbers. An $m \times n$ matrix has $m$ rows and $n$ columns.

## 2. Matrix Operations

### 1. Matrix Addition
Add corresponding elements. $\mathbf{A}$ and $\mathbf{B}$ must have the same dimensions.

### 2. Matrix Multiplication
If $\mathbf{A}$ is $m \times n$ and $\mathbf{B}$ is $n \times p$, their product $\mathbf{C} = \mathbf{A}\mathbf{B}$ is an $m \times p$ matrix.
$$ c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj} $$
**(Note: Multiplication is not commutative: $\mathbf{AB} \neq \mathbf{BA}$ in general)**

### 3. Transpose ($\mathbf{A}^T$)
Swap rows and columns.
$$ (\mathbf{A}^T)_{ij} = \mathbf{A}_{ji} $$
If $\mathbf{A}^T = \mathbf{A}$, the matrix is **Symmetric**.

### 4. Determinant ($|\mathbf{A}|$)
A scalar value associated with a square matrix.
*   For $2 \times 2$: $|\mathbf{A}| = ad - bc$.
*   If $|\mathbf{A}| = 0$, the matrix is **Singular** (not invertible).

## 3. Inverse of a Matrix ($\mathbf{A}^{-1}$)

The inverse exists if $|\mathbf{A}| \neq 0$.
$$ \mathbf{A}\mathbf{A}^{-1} = \mathbf{I} $$
where $\mathbf{I}$ is the Identity Matrix.

## 4. Rank of a Matrix

The maximum number of linearly independent rows or columns.
Used to solve systems of linear equations.

## 5. Real-World Application in CS

### 1. Computer Graphics
Matrices represent transformations: rotation, scaling, and translation of 3D objects.
$$ \begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} $$

### 2. Machine Learning
Weights in neural networks are stored as matrices. Feedforward is essentially matrix multiplication.
$$ \mathbf{Y} = \sigma(\mathbf{W}\mathbf{x} + \mathbf{b}) $$

### 3. PageRank Algorithm
Google's original algorithm uses a large matrix (Transition Matrix) to represent links between web pages.

## 6. Solved Examples

**Example 1:**
Multiply $\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $\mathbf{B} = \begin{bmatrix} 2 & 0 \\ 1 & 2 \end{bmatrix}$.

**Solution:**
$$ \begin{bmatrix} (1)(2)+(2)(1) & (1)(0)+(2)(2) \\ (3)(2)+(4)(1) & (3)(0)+(4)(2) \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ 10 & 8 \end{bmatrix} $$

**Example 2:**
Find the determinant of $\mathbf{A} = \begin{bmatrix} 2 & 5 \\ 3 & 1 \end{bmatrix}$.

**Solution:**
$$ (2)(1) - (5)(3) = 2 - 15 = -13 $$

## 7. Practice Problems

1.  Given $\mathbf{A} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$, find $\mathbf{A}^T$.
2.  Multiply $\begin{bmatrix} 1 & 2 \end{bmatrix} \times \begin{bmatrix} 3 \\ 4 \end{bmatrix}$.
3.  Compute the inverse of $\mathbf{A} = \begin{bmatrix} 4 & 7 \\ 2 & 6 \end{bmatrix}$.
