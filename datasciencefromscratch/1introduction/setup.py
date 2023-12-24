def setup_friends(users, friendships):
    for user in users:
        user["friends"] = []

    for i, j in friendships:
        # this works because users[i] is the user whose id is i
        users[i]["friends"].append(users[j]) # add i as a friend of j
        users[j]["friends"].append(users[i]) # add j as a friend of i