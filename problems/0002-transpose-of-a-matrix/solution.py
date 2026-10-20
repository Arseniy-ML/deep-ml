def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    new_matrix = [[] for _ in range(len(a[0]))]
    for row in range(len(a)):
        for col in range(len(a[0])):
            new_matrix[col].append(a[row][col])

    return new_matrix
    
    # Your code here
    pass