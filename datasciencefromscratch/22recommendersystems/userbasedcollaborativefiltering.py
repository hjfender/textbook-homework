import math

def cosine_similarity(v, w):
	return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))

def make_user_interest_vector(user_interests):
	"""given a list of interests, produce a vector whose ith element is 1
	if unique_interests[i] is in the list, 0 otherwise"""
	return [1 if interest in user_interests else 0
			for interest in unique_interests]

def most_similar_users_to(user_id):
	pairs = [(other_user_id, similarity)						# find other
			 for other_user_id, similarity in					# users with
				enumerate(user_similarities[user_id])			# nonzero
			 if user_id != other_user_id and similarity > 0]	# similarity

	return sorted(pairs,										# sort them
				  key=lambda tuple: tuple[1],					# most similar
				  reverse=True)									# first

def user_based_suggestions(user_id, include_current_interests=False):
	# sum up the similarities
	suggestions = defaultdict(float)
	for other_user_id, similarity in most_similar_users_to(user_id):
		for interest in users_interests[other_user_id]:
			suggestions[interest] += similarity

	# convert them to a sorted list
	suggestions = sorted(suggestions.dict_items(),
						 key=lambda tuple: tuple[1],
						 reversed=True)

	# and (maybe) exclude already-interests
	if include_current_interests:
		return suggestions
	else:
		return [tuple
				for tuple[0], tuple[1] in suggestions
				if tuple[0] not in user_interests[user_id]]