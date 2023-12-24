def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
print(g(3))     # 8 (== ( 3 + 1) * 2)
print(g(-1))    # 0 (== ( -1 + 1) * 2)

def f2(x, y):
    return x + y

g = doubler(f2)
print(g(1,2))   # TypeError: g() takes exactly 1 argument (2 given)
# to fix this we need to define a function that takes an arbitrary number of arguments

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)
# args is a tuple of its unnamed arguments
# kwargs is a dict of its unnamed arguments

magic(1, 2, key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: { 'key2': 'word2', 'key': 'word' }

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = { "z" : 3 }
print(other_way_magic(*x_y_list, **z_dict))  # 6

def doubler_correct(f):
    """works no matter what kind of inputs f expects"""
    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1,2)) # 6