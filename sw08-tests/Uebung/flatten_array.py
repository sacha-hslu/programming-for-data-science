
def flatten_array(array):
    result = []
    for i in array:
        if isinstance(i, list):
            result.extend(flatten_array(i))
        else:
            result.append(i)
    return result
