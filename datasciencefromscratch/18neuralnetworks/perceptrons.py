def step_function(x):
	return 1 if x>=0 else 0

def perceptron_output(weights, bias, x):
	"""returns 1 if the perceptron 'fires', 0 if not"""
	calculation = dot(weights, x) + bias
	return step_function(calculation)