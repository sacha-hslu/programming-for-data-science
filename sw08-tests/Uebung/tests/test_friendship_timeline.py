import pytest
from friendship_timeline import *

@pytest.mark.parametrize("friends_added, friends_removed, expected", [
    (
        [
            {'user_ids': [1, 2], 'created_at': '2020-01-01'},
            {'user_ids': [3, 2], 'created_at': '2020-01-02'},
            {'user_ids': [2, 1], 'created_at': '2020-02-02'},
            {'user_ids': [4, 1], 'created_at': '2020-02-02'}
        ],
        [
            {'user_ids': [2, 1], 'created_at': '2020-01-03'},
            {'user_ids': [2, 3], 'created_at': '2020-01-05'},
            {'user_ids': [1, 2], 'created_at': '2020-02-05'}
        ],
        [
            {'user_ids': [1, 2], 'start_date': '2020-01-01', 'end_date': '2020-01-03'},
            {'user_ids': [2, 3], 'start_date': '2020-01-02', 'end_date': '2020-01-05'},
            {'user_ids': [1, 2], 'start_date': '2020-02-02', 'end_date': '2020-02-05'}
        ]
    ),
    # Add more test cases as needed
])
def test_friendship_timeline(friends_added, friends_removed, expected):
    result = friendship_timeline(friends_added, friends_removed)
    assert result == expected
