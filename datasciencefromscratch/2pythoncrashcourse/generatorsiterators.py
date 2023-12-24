# creating generators with the yield operator
def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

# Python comes with a lazy_range function called xrange. In Python 3, range itself is lazy.

# the following loop will consume the yielded values one at a time until none are left
for i in lazy_range(10):
    do_something_with(i)

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

# creating generators using for comprehensions
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)


