# Vectors

## 1. Introduction

A vector is a quantity that has both **magnitude** and **direction**.
In CS and ML, vectors are essentially arrays of numbers representing features of an object.

**Notation:**
$$ \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n $$

## 2. Basic Operations

### 1. Vector Addition
$$ \mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1+v_1 \\ u_2+v_2 \\ \vdots \\ u_n+v_n \end{bmatrix} $$

### 2. Scalar Multiplication
$$ c\mathbf{v} = \begin{bmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{bmatrix} $$

### 3. Dot Product (Inner Product)
$$ \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i $$
Or geometrically:
$$ \mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta $$
Where $\theta$ is the angle between the vectors.

### 4. Norm (Magnitude)
$$ \|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2} $$
This is the Euclidean distance from the origin.

## 3. Orthogonality

Two vectors are **orthogonal** (perpendicular) if their dot product is zero.
$$ \mathbf{u} \cdot \mathbf{v} = 0 \iff \mathbf{u} \perp \mathbf{v} $$

## 4. Real-World Application in CS

### 1. Recommendation Systems
Cosine Similarity measures how similar two user vectors or item vectors are (e.g., Netflix recommendations).
$$ \cos \theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} $$
Close to 1 means very similar; close to 0 means not similar.

### 2. Computer Graphics
Vectors represent positions, directions of light, and camera orientation. Normals (orthogonal vectors) determine how light reflects off surfaces.

### 3. Natural Language Processing (NLP)
Word Embeddings (Word2Vec, GloVe) represent words as dense vectors where semantic meaning is encoded in direction.

## 5. Solved Examples

**Example 1:**
Find $\mathbf{u} \cdot \mathbf{v}$ where $\mathbf{u} = [1, 2, 3]$ and $\mathbf{v} = [4, -5, 6]$.

**Solution:**
$$ (1)(4) + (2)(-5) + (3)(6) $$
$$ 4 - 10 + 18 = 12 $$

**Example 2:**
Calculate the magnitude of $\mathbf{v} = [3, 4]$.

**Solution:**
$$ \|\mathbf{v}\| = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5 $$

## 6. Practice Problems

1.  Compute the angle between $\mathbf{u} = [1, 0]$ and $\mathbf{v} = [1, 1]$.
2.  Normalize the vector $\mathbf{v} = [3, 4]$.
3.  Are vectors $[2, 3]$ and $[-3, 2]$ orthogonal? Prove it.
