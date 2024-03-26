def only_ints(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return False
    return isinstance(a, int) and isinstance(b, int)

print(only_ints(1, 2.0))