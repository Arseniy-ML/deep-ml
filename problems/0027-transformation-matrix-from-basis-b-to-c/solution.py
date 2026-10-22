def transform_basis(B: list[list[float]], C: list[list[float]]) -> list[list[float]]:
    n = len(C)
	
    augmented = []
    for i in range(n):
        augmented.append(list(C[i]) + list(B[i]))
        
    for i in range(n):
        pivot_row = i
        for r in range(i + 1, n):
            if abs(augmented[r][i]) > abs(augmented[pivot_row][i]):
                pivot_row = r
                

        if pivot_row != i:
            augmented[i], augmented[pivot_row] = augmented[pivot_row], augmented[i]
            
        pivot = augmented[i][i]
        
      
        for j in range(i, 2 * n):
            augmented[i][j] /= pivot

        for r in range(n):
            if r != i:
                factor = augmented[r][i]
                for j in range(i, 2 * n):
                    augmented[r][j] -= factor * augmented[i][j]
                    

    P = []
    for i in range(n):
        P.append(augmented[i][n:])
        
    return P
