def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for row in matrix:
			row_mean = sum(row) / len(matrix[0])
			means.append(row_mean)
	elif mode == "column":
		num_rows = len(matrix)
		num_columns = len(matrix[0])

		for col in range(num_columns):
			column_sum = 0
			for row in range(num_rows):
				column_sum += matrix[row][col]
			
			col_mean = column_sum / num_rows
			means.append(col_mean)
	return means