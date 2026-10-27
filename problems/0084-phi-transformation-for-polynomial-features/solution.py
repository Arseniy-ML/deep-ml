import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	"""
	Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

	Args:
		data (list[float]): A list of numerical values to transform.
		degree (int): The degree of the polynomial expansion.

	"""
	result = []

	if degree < 0:
		return []

	for x in data:
		row = []
		for y in range(degree + 1):
			row.append(x ** y)
		result.append(row)

	return result
	

	# Your code here
	pass