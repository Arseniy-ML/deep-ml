
import numpy as np

def r_squared(y_true, y_pred):
    # Write your code here
    mse = np.mean((y_true - y_pred) ** 2)
    variance = np.var(y_true)
    r_squared_ = 1 - (mse / variance)
    return r_squared_
    pass
