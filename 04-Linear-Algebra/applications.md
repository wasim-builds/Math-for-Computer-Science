# Linear Algebra Applications in CS

## 1. Computer Graphics

### 1. Transformations
Everything you see on a screen involves matrix multiplication.
*   **Rotation:** Rotating an object around an axis.
*   **Scaling:** Changing the size of an object.
*   **Translation:** Moving an object.

### 2. Ray Tracing
Calculating how light rays interact with surfaces requires complex vector math (dot products for lighting, cross products for normals).

## 2. Machine Learning & AI

### 1. Neural Networks
A neural network is essentially a series of matrix multiplications and non-linear activation functions.
*   **Inputs:** Vectors representing data.
*   **Weights:** Matrices representing connections between neurons.
*   **Biases:** Vectors added to the product.

### 2. Dimensionality Reduction (PCA)
Using eigenvalues and eigenvectors to reduce the number of features in a dataset while keeping the most important information.

### 3. Singular Value Decomposition (SVD)
SVD is used in:
*   **Recommender Systems:** Latent Semantic Analysis.
*   **Image Compression:** Storing an approximation of the image using fewer singular values.

## 3. Natural Language Processing (NLP)

### 1. Word Embeddings
Representing words as dense vectors in a high-dimensional space.
*   Words with similar meanings have vectors that are close together (high cosine similarity).
*   **Analogy:** $\text{King} - \text{Man} + \text{Woman} \approx \text{Queen}$.

### 2. Latent Semantic Analysis (LSA)
Uses SVD on a term-document matrix to find hidden relationships between words and documents.

## 4. Graph Algorithms & Network Analysis

### 1. PageRank
Google's algorithm uses the eigenvector of the transition matrix of the web graph to rank pages.

### 2. Spectral Clustering
Using the eigenvalues of the Laplacian matrix of a graph to find clusters (communities) within the network.

## 5. Cryptography

### 1. Hill Cipher
A polygraphic substitution cipher based on linear algebra.
*   Encryption: $\mathbf{C} = \mathbf{K}\mathbf{P} \mod 26$
*   Decryption: $\mathbf{P} = \mathbf{K}^{-1}\mathbf{C} \mod 26$
*   Where $\mathbf{K}$ is the key matrix, $\mathbf{P}$ is the plaintext vector, and $\mathbf{C}$ is the ciphertext vector.

## 6. Quantum Computing

### 1. Qubits
Quantum states are represented by unit vectors in a complex vector space (Hilbert space).

### 2. Quantum Gates
Operations on qubits are represented by unitary matrices.
