A = [[1, 2, 3], # A has 2 rows and 3 columns
     [4, 5 ,6]]

B = [[1, 2],    # B has 3 rows and 2 columns
     [3, 4],
     [5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]     # A[i] is already the ith row

def get_column(A, j):
    return [A_i[j]           # jth element of row A_i
            for A_i in A]    # for each row A_i

def make_matrix(num_row, num_cols, entry_fn):
    """returns a num_row x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  # [entry_fn(i, 0), ..., entry_fn(i, num_cols) ]
            for i in range(num_rows)]   # create one list for each i

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)

# [[1, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0],
#  [0, 0, 1, 0, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1]]

# a 1000 x 3 matrix could be used to record the heights, weights, and ages of 1000 people
data = [[70, 170, 40],
        [65, 120, 26],
        [77, 250, 19]
        # 997 more rows
        ]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#   user 0 1 2 3 4 5 6 7 8 9
#   adjacency matrix for the friendships above
friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
               [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

friendships[0][2] == 1  # True, 0 and 2 are friends
friendships[0][8] == 1  # False, 0 and 8 are not friends

friends_of_five = [i                                                # only need
                   for id, is_friend in enumerate(friendships[5])   # to look at
                   if is_friend]                                    # one row