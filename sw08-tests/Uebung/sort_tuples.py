def sort_tuples(lst):
    # Sort based on first element in ascending order
    lst.sort(key=lambda x: x[0])

    # Sort based on second element in descending order
    lst.sort(key=lambda x: x[1], reverse=True)

    return lst
