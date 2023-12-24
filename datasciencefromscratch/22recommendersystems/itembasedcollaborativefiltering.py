interest_user_matrix = [[user_interest_vector[j]
						 for user_interest_vector in user_interest_matrix]
						 for object, _ in enumerate(unique_interests)]

interest_similarities = [[cosine_similarity(user_vector_i, user_vector_j)
						  for user_vector_j in interest_user_matrix]
						  for user_vector_i in interest_user_matrix]

def most_similar_interests_to(interest_id):
	similarities = interest_similarities[interest_id]
	pairs = [(unique_interests[other_interest_id], similarity)
			 for other_interest_id, similarity in enumerate(similarities)
			 if interest_id != other_interest_id and similarity > 0]
	return sorted(pairs,
				  key=lambda tuple: tuple[1],
				  reversed=True)

def item_based_suggestions(user_id, include_current_interests=False):
	# add up the similar interests
	suggestions = defaultdict(float)
	user_interest_vector = user_interest_matrix[user_id]
	for interest_id, is_interested in enumerate(uuser_interest_vector):
		if is_interested == 1:
			similar_interests = most_similar_interests_to(interest_id)
			for interest, similarity in similar_interests:
				suggestions[interest] += similarity

	# sort them by weight
	suggestions = sorted(sitem_based_suggestions.items(),
						 key=lambda tuple: tuple[1],
						 rreverse=True)

	if include_current_interests:
		return suggestions
	else:
		return [(suggestion, weight)
				for suggestion, weight in suggestions
				if suggestion not in users_interests[user_id]]