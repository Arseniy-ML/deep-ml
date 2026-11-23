import numpy as np


def soft_threshold(w: np.ndarray, threshold: float) -> np.ndarray:
  return np.sign(w) * np.maximum(np.abs(w) - threshold, 0.0)


def l1_regularization_gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    alpha: float = 0.1,
    learning_rate: float = 0.01,
    max_iter: int = 1000,
    tol: float = 1e-4,
) -> tuple:
  n_samples, n_features = X.shape
  w = np.zeros(n_features)
  b = 0.0

  for _ in range(max_iter):
    w_old = w.copy()

    y_pred = X @ w + b
    errors = y_pred - y

    dw = (1 / n_samples) * (X.T @ errors)
    db = (1 / n_samples) * np.sum(errors)

    w = soft_threshold(w - learning_rate * dw, learning_rate * alpha)
    b = b - learning_rate * db

    if np.linalg.norm(w - w_old) < tol:
      break

  return w, float(b)
