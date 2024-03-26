"""
This module contains the function 'friendship_timeline'
that takes two lists of dictionaries and returns a list of dictionaries.

"""

def friendship_timeline(friends_added, friends_removed):
    """_summary_

    Args:
        friends_added (list of dictionaries): shows the date when two users became friends
        friends_removed (list of dictionaries): shows the date when two users stopped being friends

    Returns:
        friendships (list of dictionaries): shows the date when two users became friends
        and when they stopped being friends
    """
    # Sort the lists by 'created_at'
    friends_added.sort(key=lambda x: x['created_at'])
    friends_removed.sort(key=lambda x: x['created_at'])

    friendships = []

    for removed in friends_removed:
        for added in friends_added:
            # Check if the 'user_ids' match
            if set(removed['user_ids']) == set(added['user_ids']):
                # Create a new dictionary and add it to the 'friendships' list
                friendships.append({
                    'user_ids': sorted(removed['user_ids']),
                    'start_date': added['created_at'],
                    'end_date': removed['created_at']
                })
                # Remove the item from 'friends_added'
                friends_added.remove(added)
                break

    return friendships
