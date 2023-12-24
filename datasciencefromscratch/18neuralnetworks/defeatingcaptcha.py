zero_digit = [1,1,1,1,1,
			  1,0,0,0,1,
			  1,0,0,0,1,
			  1,0,0,0,1,
			  1,1,1,1,1]

one_digit = [0,0,1,0,0,
			 0,0,1,0,0,
			 0,0,1,0,0,
			 0,0,1,0,0,
			 0,0,1,0,0]

two_digit = [1,1,1,1,1,
			 0,0,0,0,1,
			 1,1,1,1,1,
			 1,0,0,0,0,
			 1,1,1,1,1]

three_digit = [1,1,1,1,1,
			   0,0,0,0,1,
			   1,1,1,1,1,
			   0,0,0,0,1,
			   1,1,1,1,1]

four_digit = [1,0,0,0,1,
			  1,0,0,0,1,
			  1,1,1,1,1,
			  0,0,0,0,1,
			  0,0,0,0,1]

five_digit = [1,1,1,1,1,
			  1,0,0,0,0,
			  1,1,1,1,1,
			  0,0,0,0,1,
			  1,1,1,1,1]

six_digit = [1,1,1,1,1,
			 1,0,0,0,0,
			 1,1,1,1,1,
			 1,0,0,0,1,
			 1,1,1,1,1]

seven_digit = [1,1,1,1,1,
			   0,0,0,0,1,
			   0,0,0,0,1,
			   0,0,0,0,1,
			   0,0,0,0,1]

eight_digit = [1,1,1,1,1,
			   1,0,0,0,1,
			   1,1,1,1,1,
			   1,0,0,0,1,
			   1,1,1,1,1]

nine_digit = [1,1,1,1,1,
			  1,0,0,0,1,
			  1,1,1,1,1,
			  0,0,0,0,1,
			  1,1,1,1,1]

inputs = [zero_digit, one_digit, two_digit, three_digit, four_digit,
		  five_digit, six_digit, seven_digit, eight_digit, nine_digit]

targets = [[1 if i == j else 0 for i in range(10)]
		   for j in range(10)]

random.seed(0)		# to get repeatable results
input_size = 25		# each input is a vector of length 25
num_hidden = 5		# we'll have 5 neurons in the hidden layer
output_size = 10	# we need 10 outputs for each input

# each hidden neuron has one weight per input, plus a bias weight
hidden_layer = [[random.random() for _ in range(input_size + 1)]
				for _ in range(num_hidden)]

# each output neuron has one weight per hidden neuron, plus a bias weight
output_layer = [[random.random() for _ in range(num_hidden + 1)]
				for _ in range(output_size)]

# the network starts out with randome weights
network = [hidden_layer, output_layer]

# 10,000 iterations seems enough to converge
for _ in range(10000):
	for input_vector, target_vector in zip(iinput_size, targets):
		backpropagate(network, input_vector, target_vector)

def predict(input):
	return feed_forward(network, input)[-1]

predict(inputs[7])
# [0.026, 0.0, 0.0, 0.010, 0.001, 0.0, 0.0, 0.967, 0.0, 0.0]

# predicting a stylized '3'
predict([0,1,1,1,0,
		 0,0,0,1,1,
		 0,0,1,1,0,
		 0,0,0,1,1,
		 0,1,1,1,0])
# it thinks it is a '3'
# [0.0, 0.0, 0.0, 0.92, 0.0, 0.0, 0.0, 0.01, 0.0, 0.12]

# predicting a stylized '8'
predict([0,1,1,1,0,
		 1,0,0,1,1,
		 0,1,1,1,0,
		 1,0,0,1,1,
		 0,1,1,1,0])
# it thinks it is a '5', '8', and '9'
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.55, 0.0, 0.0, 0.93, 1.0]

import matplotlib
weights = network[0][0]						# first neuron in hidden layer
abs_weights = map(abs, weights)				# darkness only depends on absolute value

grid = [abs_weights[row:(row+5)]			# turn the weights into a 5x5 grid
		for row in range(0,25,5)]			# [weights[0:5], ..., weights[20:25]

ax = plt.gca()								# to use hatching, we'll need the axis

ax.imshow(grid,								# here same as plt.imshow
		  cmap = matplotlib.cm.binary,		# use white-black color scale
		  interpolation = 'none')			# plot blocks as blocks

def patch(x, y, hatch, color):
	"""return a matplotlib 'patch' object with the specified
	location, crosshatch pattern, and color"""
	return matplotlib.patches.Rectangle((x - 0.5, y - 0.5), 1, 1,
										hatch=hatch, fill=False, color=color)

# cross-hatch the negative weights
for i in range(5):					# row
	for j in range(5):				# column
		if weights[5*i + j] < 0:	# row i, column j = weights[5*i + j]
			# add black and white hatches, so visible wheter dark or light
			ax.add_patch(patch(j, i, '/', "white"))
			ax.add_patch(patch(j, i, '\\', "black"))

plt.show()

left_column_only = [1, 0, 0, 0, 0] * 5
print(feed_forward(network, left_column_only)[0][0])	# 1.0

center_middle_row = [0, 0, 0, 0, 0] * 2 + [0, 1, 1, 1, 0] + [0, 0, 0, 0, 0] * 2
print(feed_forward(network, center_middle_row)[0][0])	# 0.95

right_column_only = [0, 0, 0, 0, 1] * 5
print(feed_forward(network, right_column_only)[0][0])	# 0.0