
from flatten_array import *

def test_flatten_array():
    # Test empty list
    assert flatten_array([]) == []

    # Test 1D list
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

    # Test nested list
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

    # Test deeply nested list
    assert flatten_array([1, [2, [3, [4]]]]) == [1, 2, 3, 4]

    # Test list with multiple types
    assert flatten_array([1, [2, '3'], {'four': 4}]) == [1, 2, '3', {'four': 4}]
