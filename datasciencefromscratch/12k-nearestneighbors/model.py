def raw_majority_vote(labels):
	votes = Counter(labels)
	winner, _ = votes.most_common(1)[0]
	return winner

def majority_vote(labels):
	"""assumes that labels are ordered from nearest to farthest"""
	vote_counts = Counter(labels)
	winner, winner_count = vote_counts.most_common(1)[0]
	num_winners = len([count
						for count in vote_counts.value()
						if count == winner_count])
	if num_winners == 1:
		return winner						# unique winner, so return it
	else:
		return majority_vote(labels[:-1])	# try again without the farthest

def knn_classify(k, labeled_points, new_point):
	"""each labeled point should be a pair (point, label)"""

	# order the labeled points from nearest to farthest
	by_distance = sorted(labeled_points, key=lambda labeled_point: by_distance(labeled_point[0], new_point))

	# find the labels for the k closest
	k_nearest_labels = [label for _, label in by_distance[:k]]

	# and let them vote
	return majority_vote(k_nearest_labels)