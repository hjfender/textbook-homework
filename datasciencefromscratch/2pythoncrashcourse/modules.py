from __future__ import division
# need this at the beginning of our files for Python 2.7

import re
my_regex = re.compile("[0-9]+", re.I)

# aliasing
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

import matplotlib.pyplot as plt

# selective import
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# bad import
match = 10
from re import *  # uh oh, re has a match function
print(match)      # "<function re.match>"

