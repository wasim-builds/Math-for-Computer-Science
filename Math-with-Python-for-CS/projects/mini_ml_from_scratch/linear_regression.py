import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Training loop:
        1. Initialize parameters (weights, bias)
        2. Predict y_hat = wX + b
        3. Calculate gradients (dw, db)
        4. Update parameters: w = w - lr*dw, b = b - lr*db
        """
        n_samples, n_features = X.shape
        
        # Initialize parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Derivatives (Gradients)
            # dw = (1/N) * 2 * X.T * (y_predicted - y)
            # db = (1/N) * 2 * sum(y_predicted - y)
            
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            
            # Update parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# Testing the implementation
if __name__ == "__main__":
    from sklearn.model_selection import train_test_split
    from sklearn import datasets

    # Generate synthetic data
    X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    # Train Model
    regressor = LinearRegression(learning_rate=0.01, n_iters=1000)
    regressor.fit(X_train, y_train)
    predicted = regressor.predict(X_test)

    # Calculate MSE
    mse = np.mean((y_test - predicted)**2)
    print(f"Mean Squared Error: {mse:.4f}")

    # Plotting
    y_pred_line = regressor.predict(X)
    cmap = plt.get_cmap('viridis')
    fig = plt.figure(figsize=(8,6))
    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(X, y_pred_line, color='black', linewidth=2, label="Prediction")
    plt.show()
