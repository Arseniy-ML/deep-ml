import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	values_array = []
	column_indices_array = []
	row_pointer_array = [0]
	non_zero_count = 0

	for r, row in enumerate(dense_matrix):
		for c, val in enumerate(row):
			if val != 0:
				values_array.append(val)
				column_indices_array.append(c)
				non_zero_count += 1

		row_pointer_array.append(non_zero_count)

	return (
		values_array,
		column_indices_array,
		row_pointer_array
	)

	

	
	pass
