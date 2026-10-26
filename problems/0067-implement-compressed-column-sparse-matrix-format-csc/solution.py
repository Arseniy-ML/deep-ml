def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	if not dense_matrix or not dense_matrix[0]:
		return [], [], [0]

	values_array = []
	row_indices_array = []
	col_pointer_array = [0]
	non_zero_count = 0

	num_columns = len(dense_matrix[0])
	num_rows = len(dense_matrix)

	for c in range(num_columns):
		for r in range(num_rows):
			element = dense_matrix[r][c]

			if element != 0:
				values_array.append(element)
				row_indices_array.append(r)
				non_zero_count += 1

		col_pointer_array.append(non_zero_count)

	return (
		values_array,
		row_indices_array,
		col_pointer_array
	)
	pass
