import random

random.seed(0)
x_train, x_test, y_train, y_test = train_test_split(rescaled_x, y_test, 0.33)

# want to maximize log likelihood on the training data
fn = partial(logistic_log_likelihood, x_train, y_train)
gradient_fn = partial(logistic_log_gradient, x_train, y_train)

# pick a random starting point
beta_0 = [random.random() for _ in range(3)]

# and maximize using gradient descent
beta_hat = maximize_batch(fn, gradient_fn, beta_0)

# or with stochastic gradient descent
beta_hat = maximize_stochastic(logistic_log_likelihood_i,
							   logistic_log_gradient_i,
							   x_train, y_train, beta_0)

# Goodness of Fit
true_positives = false_positive = true_negative = false_negatives = 0

for x_i, y_i in zip(x_test, y_test):
	predict = logistic(dot(beta_hat, x_i))

	if y_i == 1 and predict >= 0.5:		# TP: paid and we predict paid
		true_positives += 1
	elif y_i == 1:						# FN: paid and we predict unpaid
		false_negatives += 1
	elif predict >= 0.5:				# FP: unpaid and we predict paid
		false_positive += 1
	else:								# TN: unpaid and we predict unpaid
		true_negatives += 1

precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)