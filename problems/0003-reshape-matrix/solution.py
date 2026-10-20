import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # Write your code here and return a python list after
    # reshaping by using numpy's tolist() method
    reshaped_matrix = np.array(a)
    new_rows, new_cols = new_shape
    

    if new_rows <= 0 or new_cols <= 0 or reshaped_matrix.size != (new_rows * new_cols):
        return []
    else:
        return reshaped_matrix.reshape(new_shape).tolist()
