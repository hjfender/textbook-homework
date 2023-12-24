from __future__ import division # replaces integer division with floating point division - NOT Working for some reason
from setup import setup_friends

def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"]) # length of friend_ids list

def get_total_connections(users):
    return sum(number_of_friends(user) for user in users) # 24

def get_avg_connections(users):
    total_connections = get_total_connections(users)
    num_users = len(users)                         # length of the users list
    return total_connections / num_users # 2.4

def get_list_num_friends_by_id(users):
    """create a list (user_id, number_of_friends)"""
    return [(user["id"], number_of_friends(user)) for user in users]

def sort_list_by_num_friends(num_friends_by_id):
    return sorted(num_friends_by_id,                              # get it sorted
                key=lambda user: user[1],                         # by num_friends
                reverse=True)                                     # largest to smallest
    # each pair is (user_id, num_friends)
    # [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
    #  (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

# this is the DEGREE CENTRALITY of the network

def main():
    from users import users, friendships
    setup_friends(users, friendships)
    total_connections = get_total_connections(users)
    print('Total connections: %(total_connections)i\n' % { 'total_connections': total_connections })
    avg_connections = get_avg_connections(users)
    print('Average connections: %(avg_connections).1f\n' % { 'avg_connections' : avg_connections })
    print('Degree Centrality List')
    sorted_list = sort_list_by_num_friends(get_list_num_friends_by_id(users))
    for i, j in sorted_list:
        print('- User: %(i)i, Friends: %(j)i' % { 'i': i, 'j': j})

main()