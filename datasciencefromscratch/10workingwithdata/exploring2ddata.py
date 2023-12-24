import random
path_to_repo = re.sub('10workingwithdata', '', sys.path[0])
sys.path.insert(0, path_to_repo + '6probability')
sys.path.insert(0, path_to_repo + '5statistics')
from continuousdistribuitions import inverse_normal_cdf
from correlation import correlation
from matplotlib import pyplot as plt

def random_normal():
	"""returns a random draw from a standard normal distribution"""
	return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=0)
plt.title("Very Different Joint Distributions")
plt.show()

print(correlation(xs, ys1))	#  0.9
print(correlation(xs, ys2))	# -0.9