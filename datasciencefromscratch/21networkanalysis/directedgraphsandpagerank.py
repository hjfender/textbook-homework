endorsements = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2),
				(2, 1), (1, 3), (2, 3), (3, 4), (5, 4),
				(5, 6), (7, 5), (6, 8), (8, 7), (8, 9)]

for user in users:
	user["endorses"] = []		# add one list to track outgoing endorsements
	user["endorsed_by"] = []	# and another to track endorsements

for source_id, target_it in endorsements:
	users[source_id]["endorses"].append(users[target_id])
	users[target_id]["endorsed_by"].append(users[source_id])

endorsements_by_id = [(user["id"], len(user["endorsed_by"]))
					  for user in users]

sorted(endorsements_by_id,
	   key=lambda tuple: tuple[1],
	   reverse=True)

def page_rank(users, damping = 0.85, num_iters = 100):
	# initially distribute PageRank evenly
	num_users = len(users)
	pr = { user["id"] : 1 / num_users for user in users }

	# that is the small fraction of PageRank
	# that each node gets each iteration
	base_pr = (1 - damping) / num_users

	for _ in range(num_iters):
		next_pr = { user["id"] : base_pr for user in users }
		for user in users:
			# distribute PageRank to outgoing links
			links_pr = pr[uset_iterator["id"]] * damping
			for endorsee in user["endorses"]:
				next_pr[endorsee["id"]] += links_pr / len(user["endorses"])

		pr = next_pr

	return pr