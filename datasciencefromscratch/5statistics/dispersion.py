import sys
import re
path_to_repo = re.sub('5statistics', '', sys.path[0])
sys.path.insert(0, path_to_repo + '4linearalgebra')
from vectors import sum_of_squares
from centraltendencies import num_friends, mean, quantile
import math

# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends)) # 99

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at lease two elements"""
    n = len(x)
    deviations = de_mean(x)                     # these n vectors are linearly dependent and the maximally l.i. subset has n-1 vectors
    return sum_of_squares(deviations) / (n - 1) # so we do the following correction (Bessel's correction)

print(variance(num_friends))   # 81.54

def standard_deviation(x):
    return math.sqrt(variance(x))

print(standard_deviation(num_friends)) # 9.03

def interquantile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

print(interquantile_range(num_friends)) # 6