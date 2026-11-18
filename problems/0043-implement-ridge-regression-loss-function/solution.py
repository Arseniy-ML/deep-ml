import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    n = X.shape[0]
    residual = y_true - X @ w
    mse = np.sum(residual ** 2) / n
    penalty = alpha * np.sum(w ** 2)
    return float(mse + penalty)
    # Your code here
    pass
