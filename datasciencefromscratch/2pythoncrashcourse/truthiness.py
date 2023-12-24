one_is_less_than_two = 1 < 2
true_equals_false = True == False

x = None
print(x == None) # prints True, but is not Pythonic
print(x is None) # prints True, but is Pythonic

# a lot of things are treated as 'true' in Python
s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

# simpler version of the above
first_char = s and s[0]

safe_x = x or 0

# The following list is for those values that are 'falsy'
# - False
# - None
# - []
# - {}
# - ""
# - set()
# - 0
# - 0.0

# all function returns true when every items in the list is true
# any function returns true when any item in the list is true
all([True, 1, { 3 }])   # True
all([True, 1, {}])      # False, {} is falsy
any()                   # True, True is truthy
all([])                 # True, no falsy elements in the list
any([])                 # False, no truthy elements in the list