# Eigenvalues and Eigenvectors

## 1. Definition

An **eigenvector** of a square matrix $\mathbf{A}$ is a non-zero vector $\mathbf{v}$ such that multiplication by $\mathbf{A}$ alters only its scale, not its direction.

$$ \mathbf{A}\mathbf{v} = \lambda\mathbf{v} $$

*   $\mathbf{v}$: Eigenvector
*   $\lambda$: Eigenvalue (scalar)

## 2. Calculation

To find eigenvalues, solve the characteristic equation:
$$ \det(\mathbf{A} - \lambda\mathbf{I}) = 0 $$

Once $\lambda$ is found, substitute it back into $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}$ to find the eigenvector $\mathbf{v}$.

## 3. Properties

1.  The sum of eigenvalues equals the trace of the matrix (sum of diagonal elements).
    $$ \sum \lambda_i = \text{tr}(\mathbf{A}) $$
2.  The product of eigenvalues equals the determinant of the matrix.
    $$ \prod \lambda_i = \det(\mathbf{A}) $$

## 4. Eigendecomposition

If a matrix $\mathbf{A}$ has $n$ linearly independent eigenvectors, it can be diagonalized:
$$ \mathbf{A} = \mathbf{Q}\mathbf{\Lambda}\mathbf{Q}^{-1} $$
Where $\mathbf{Q}$ is the matrix of eigenvectors and $\mathbf{\Lambda}$ is the diagonal matrix of eigenvalues.

## 5. Real-World Application in CS

### 1. Principal Component Analysis (PCA)
In Data Science, PCA reduces the dimensionality of data while preserving variance. The principal components are the eigenvectors of the covariance matrix corresponding to the largest eigenvalues.

### 2. Google's PageRank
The entire web is modeled as a graph. The PageRank score of a website is the dominant eigenvector of the transition matrix.

### 3. Face Recognition (Eigenfaces)
Images are represented as vectors. Eigenfaces are the eigenvectors of the covariance matrix of the set of face images, used to recognize faces.

## 6. Solved Examples

**Example 1:**
Find eigenvalues of $\mathbf{A} = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$.

**Solution:**
$$ \det(\mathbf{A} - \lambda\mathbf{I}) = \det \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} = 0 $$
$$ (4-\lambda)(3-\lambda) - (1)(2) = 0 $$
$$ \lambda^2 - 7\lambda + 12 - 2 = 0 $$
$$ \lambda^2 - 7\lambda + 10 = 0 $$
$$ (\lambda - 5)(\lambda - 2) = 0 $$
Eigenvalues: $\lambda_1 = 5, \lambda_2 = 2$.

## 7. Practice Problems

1.  Find the eigenvectors for $\lambda=5$ in the example above.
2.  Prove that if $\lambda$ is an eigenvalue of $\mathbf{A}$, then $\lambda^2$ is an eigenvalue of $\mathbf{A}^2$.
3.  Calculate the trace and determinant of $\mathbf{A}$ using its eigenvalues.
