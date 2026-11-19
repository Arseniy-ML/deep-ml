import numpy as np

def k_nearest_neighbors(points, query_point, k):
    if not points or k <= 0:
        return []

    pts = np.array(points)
    q = np.array(query_point)

    distances = np.sqrt(np.sum((pts - q) ** 2, axis=1))
    sorted_indices = np.argsort(distances, kind="stable")
    nearest_k = sorted_indices[:k]
    return [points[i] for i in nearest_k]
    """
    Find k nearest neighbors to a query point
    
    Args:
        points: List of tuples representing points [(x1, y1), (x2, y2), ...]
        query_point: Tuple representing query point (x, y)
        k: Number of nearest neighbors to return
    
    Returns:
        List of k nearest neighbor points as tuples
        When distances are tied, points appearing earlier in the input list come first.
    """
    pass