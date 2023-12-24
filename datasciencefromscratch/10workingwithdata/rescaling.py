import math
import re
import sys
path_to_repo = re.sub('10workingwithdata', '', sys.path[0])
sys.path.insert(0, path_to_repo + '4linearalgebra')
sys.path.insert(0, path_to_repo + '5statistics')
from centraltendencies import mean
from dispersion import standard_deviation
from matrices import shape, get_column, make_matrix

data = { "A" :{
		"Height (inches)" : 63,
		"Height (centimeters)" : 160,
		"Weight (pounds)" : 150
	},
		"B" : {
		"Height (inches)" : 67,
		"Height (centimeters)" : 170.2,
		"Weight (pounds)" : 160
	},
		"C" : {
		"Height (inches)" : 70,
		"Height (centimeters)" : 177.8,
		"Weight (pounds)" : 171
	}
}

def distance(v1, v2):
	return math.sqrt(sum([(x-y) ** 2 for x,y in zip(v1, v2)]))

inchesA = [data["A"]["Height (inches)"], data["A"]["Weight (pounds)"]]
inchesB = [data["B"]["Height (inches)"], data["B"]["Weight (pounds)"]]
inchesC = [data["C"]["Height (inches)"], data["C"]["Weight (pounds)"]]

a_to_b = distance(inchesA, inchesB)	# 10.77
a_to_c = distance(inchesA, inchesC)	# 22.14
b_to_c = distance(inchesB, inchesC) # 11.40

print("Height (inches) A to B: ", a_to_b)
print("Height (inches) A to C: ", a_to_c)
print("Height (inches) B to C: ", b_to_c)

centisA = [data["A"]["Height (centimeters)"], data["A"]["Weight (pounds)"]]
centisB = [data["B"]["Height (centimeters)"], data["B"]["Weight (pounds)"]]
centisC = [data["C"]["Height (centimeters)"], data["C"]["Weight (pounds)"]]

a_to_b = distance(centisA, centisB) # 14.28
a_to_c = distance(centisA, centisC) # 27.53
b_to_c = distance(centisB, centisC) # 13.37

print("Height (centimeters) A to B: ", a_to_b)
print("Height (centimeters) A to C: ", a_to_c)
print("Height (centimeters) B to C: ", b_to_c)

def scale(data_matrix):
	"""returns the means and standard deviations of each column"""
	num_rows, num_cols = shape(data_matrix)
	means = [mean(get_column(data_matrix,j))
			for j in range(num_cols)]
	stdevs = [standard_deviation(get_column(data_matrix, j))
			for j in range(num_cols)]
	return means, stdevs

def rescale(data_matrix):
	"""rescales the input data so that each column
	has mean 0 and standard deviation 1
	leaves alone columns with no deviation"""
	means, stdevs = scale(data_matrix)

	def rescaled(i, j):
		if stdevs[j] > 0:
			return (data_matrix[i][j] - means[j]) / stdevs[j]
		else:
			return data_matrix[i][j]

	num_rows, num_cols = shape(data_matrix)
	return make_matrix(num_rows, num_cols, rescaled)