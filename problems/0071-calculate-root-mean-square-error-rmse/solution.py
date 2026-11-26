
import numpy as np

def rmse(y_true, y_pred):
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    if len(y_true) == 0 and len(y_pred) == 0:
        raise ValueError
    elif y_pred.shape != y_true.shape:
        raise ValueError

    rmse_res = np.sqrt(np.mean((y_true - y_pred) ** 2))
    # Write your code here
    return round(rmse_res,3)
