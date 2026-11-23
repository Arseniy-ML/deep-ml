import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # Your code here
    w = weights.copy().astype(float)
    m = X.shape[0]

    if method == 'batch':
        step = m
    elif method == 'stochastic':
        step = 1
    elif method == 'mini_batch':
        step = batch_size
    
    for _ in range(n_epochs):
        for i in range(0, m, step):
            X_b = X[i : i + step]
            y_b = y[i : i + step]
            k = len(X_b)
            predictions = X_b @ w
            errors = predictions - y_b
            gradient = (2 / k) * (X_b.T @ errors)
            w = w - learning_rate * gradient

    return w
    pass
