# example of currying
def exp(base, power):
    return base ** power

def two_to_the(power):
    return exp(2, power)

# using functools
from functools import partial
two_to_the = partial(exp, 2)    # is now a function of one variable
print(two_to_the(3))            # 8

square_of = partial(exp, power=2)
print(square_of(3))             # 9

def double(x):
    return 2 * x

# map, reduce, and filter are functional alternatives to list comprehension
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]      # [2, 4, 6, 8]
twice_xs = map(double, xs)              # same as above
list_doubler = partial(map, double)     # *function* that doubles a list
twice_xs = list_doubler(xs)             # again [2, 4, 6, 8]

def multiply(x, y): return x * y

products = map(multiply, [1, 2], [4, 5])    # [1 * 4, 2 * 5] = [4, 10]

def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs)           # same as above
list_evener = partial(filter, is_even)  # *function* that filters a list
x_evens = list_evener(xs)               # again [2, 4]

from functools import reduce

x_product = reduce(multiply, xs)            # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply)    # *function* that reduces a list
x_product = list_product(xs)                # again = 24