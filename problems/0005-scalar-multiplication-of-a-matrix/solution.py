def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []
	
	for row in matrix:
		resulting_matrix = []
		for element in row:
			resulting_matrix.append(element * scalar)
		result.append(resulting_matrix)

	return result
	pass