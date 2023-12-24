import sys
import re
path_to_repo = re.sub('5statistics', '', sys.path[0])
sys.path.insert(0, path_to_repo + '4linearalgebra')
from vectors import dot
from dispersion import de_mean
from centraltendencies import num_friends

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

# daily_minutes is an imaginary list that records the number of minutes each user spends per day on the site

#print(covariance(num_friends, daily_minutes)) # 22.43

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

#print(correlation(num_friends, daily_minutes)) # 0.25

# internal test account no one bothered to remove
outlier = num_friends.index(100)    # index of outlier

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

#daily_minutes_good = [x
#                      for id, x in enumerate(daily_minutes)
#                      if i != outlier]

#print(correlation(num_friends_good, daily_minutes_good))   # 0.57