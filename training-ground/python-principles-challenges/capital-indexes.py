def capital_indexes(text):
    result = []
    i = 0
    for letter in text:
        if letter.isupper():
            result.append(i)
        i += 1
    print(result)

capital_indexes("sAcHa vOGeL")