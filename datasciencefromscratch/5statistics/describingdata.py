from matplotlib import pyplot as plt
from collections import Counter
from scipy import stats
import random

num_friends = [100, 49, 41, 40, 25,
               21, 21, 19, 19, 18,
               18, 16, 15, 15, 15,
               15, 14, 14, 13, 13,
               13, 13, 12, 12, 11,
               10, 10, 10, 10, 10,
               10, 10, 10, 10, 10,
               10, 10, 10, 10, 10,
               9, 9, 9, 9, 9,
               9, 9, 9, 9, 9,
               9, 9, 9, 9, 9,
               9, 9, 9, 8, 8,
               8, 8, 8, 8, 8,
               8, 8, 8, 8, 8,
               8, 7, 7, 7, 7,
               7, 7, 7, 7, 7,
               7, 7, 7, 7, 7,
               7, 6, 6, 6, 6,
               6, 6, 6, 6, 6,
               6, 6, 6, 6, 6,
               6, 6, 6, 6, 6,
               6, 6, 6, 5, 5,
               5, 5, 5, 5, 5,
               5, 5, 5, 5, 5,
               5, 5, 5, 5, 5,
               4, 4, 4, 4, 4,
               4, 4, 4, 4, 4,
               4, 4, 4, 4, 4,
               4, 4, 4, 4, 4,
               3, 3, 3, 3, 3,
               3, 3, 3, 3, 3,
               3, 3, 3, 3, 3,
               3, 3, 3, 3, 3,
               2, 2, 2, 2, 2,
               2, 2, 2, 2, 2,
               2, 2, 2, 2, 2,
               2, 2, 1, 1, 1,
               1, 1, 1, 1, 1,
               1, 1, 1, 1, 1,
               1, 1, 1, 1, 1,
               1, 1, 1, 1
               ]

max_friends = max(num_friends)

friend_counts = Counter(num_friends)
xs = range(101)                         # largest value is 100
ys = [friend_counts[x] for x in xs]     # height is just # of friends
max_y = max(ys)
plt.bar(xs, ys)
plt.axis([0, 101, 0, max_y])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)       # 204
largest_value = max(num_friends)    # 100
smallest_value = min(num_friends)   # 1
print(num_points)
print(largest_value)
print(smallest_value)

sorted_values = sorted(num_friends)
smallest_values = sorted_values[0]      # 1
second_smallest_value = sorted_values[1]    # 1
second_largest_value = sorted_values[-2]    # 49
print(smallest_values)
print(second_smallest_value)
print(second_largest_value)
