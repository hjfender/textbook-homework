def entry_fn(i, j):
	return 1 if (i, j) in friendships or (j, i) in friendships else 0

n = len(users)
adjacency_matrix = make_matrix(n, n, entry_fn)

eigenvector_centralities, _ = find_eigenvector(adjacency_matrix)

matrix_operate(adjacency_matrix, eigenvector_centralities)

dot(get_row(adjacency_matrix, i), eigenvector_centralities)