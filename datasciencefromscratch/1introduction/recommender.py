from users import users, friendships
from setup import setup_friends
from interests import interests
from collections import Counter, defaultdict # not loaded by default

setup_friends(users, friendships)

# BAD first take at recommending friends to users
# it recommends the user itself and repeats recommendations
def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friend"]    # for each of user's friends
            for foaf in friend["friend"]]   # get each of _their_ friends

print([friend["id"] for friend in users[0]["friends"]]) # [1, 2]
print([friend["id"] for friend in users[1]["friends"]]) # [0, 2, 3]
print([friend["id"] for friend in users[2]["friends"]]) # [0, 1, 3]

# SECOND attempt accounting for the lessons we learned above
def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
                for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                    for friend in user["friends"] # for each of my friends
                    for foaf in friend["friends"] # count *their* friends
                    if not_the_same(user, foaf)   # who aren't me
                    and not_friends(user, foaf))  # and aren't my friends

print(friends_of_friend_ids(users[3]))             # Counter({0: 2, 5: 1})

# attempt based on interests
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

#keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
            for interest in interests_by_user_id[user["id"]]
            for interested_user_id in user_ids_by_interest[interest]
            if interested_user_id != user["id"])