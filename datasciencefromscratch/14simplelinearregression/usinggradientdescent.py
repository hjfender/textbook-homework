def squared_error(x_i, y_i, theta):
	alpha, beta = theta
	return error(alpha, beta, x_i, y_i) ** 2

def squared_error_gradient(x_i, y_i, theta):
	alpha, beta = theta
	return [-2 * error(alpha, beta, x_i, y_i),			# alpha partial derivative
			-2 * error(alpha, beta, x_i, y_i) * x_i]	# beta partial derivative

# choose random value to start
random.seed(0)
theta = [random.random(), random.random()]
alpha, beta = minimize_stochastic(squared_error,
								  squared_error_gradient,
								  num_friends_good,
								  daily_minutes_good,
								  theta,
								  0.0001)
print(alpha, beta)