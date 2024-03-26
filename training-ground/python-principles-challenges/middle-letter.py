def mid(text):
    if (len(text) % 2) == 0:
        return ""
    i = int((len(text) + 1) / 2 - 1)
    return text[i]

mid("a")