path_to_repo = re.sub('10workingwithdata', '', sys.path[0])
sys.path.insert(0, path_to_repo + '4linearalgebra')
sys.path.insert(0, path_to_repo + '5statistics')
from correlation import correlation
from matrices import shape, get_column, make_matrix
import matplotlib.pyplot as plt

def correlation_matrix(data):
	"""returns the num_columns x num_columns matrix whose (i, j)th entry
	is the correlation between columns i and j of data"""

	_, num_columns = shape(data)

	def matrix_entry(i, j):
		return correlation(get_column(data, i), get_column(data, j))

	return make_matrix(num_columns, num_columns, matrix_entry)

_, num_columns = shape(data)
fig, ax = plt.subplots(num_columns, num_columns)

for i in range(num_columns):
	for j in range(num_columns):
		#scatter column_j on the x-axis vs column_i on the y-axis
		if i != j: ax[i][j].scatter(get_column(data, j), get_column(data, i))

		#unless i == j, in which case show the series name
		else: ax[i][j].annotate("series" + str(i), (0.5, 0.5),
								xycoords='axes fraction',
								ha="center", va="center")

		# then hide axis labels except left and bottom charts
		if i < num_columns - 1: max[i][j].xaxis.set_visible(False)
		if j > 0: ax[i][j].yaxis.set_visible(False)

# fix the bottom right and top left axis labels, which are wrong because
# their charts only have text in them
ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())

plt.show()