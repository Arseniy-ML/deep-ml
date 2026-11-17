import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    mean = np.mean(data, axis=0)
    standart = np.std(data, axis=0)
    standardized_data = (data - mean) / standart

    xmin = np.min(data, axis=0)
    xmax = np.max(data, axis=0)
    normalized_data = (data - xmin) / (xmax - xmin)
    # Your code here
    return standardized_data, normalized_data