def is_anagram(a, b):
    for l in a:
        if dict.get(l) is not None:
            dict[l] = dict.get(l) + 1


    print(dict)
    print(b)

print(is_anagram("typhoon", "opython"))