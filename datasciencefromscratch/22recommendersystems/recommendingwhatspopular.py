popular_interests = Counter(interest
							for user_interests in users_interests
							for interest in user_interests).most_common()

def most_popular_new_interests(user_interests, max_results = 5):
	suggestions = [(interest, frequency)
					for interest, frequency in popular_interests
					if interest not in user_interests]
	return suggestions[:max_results]