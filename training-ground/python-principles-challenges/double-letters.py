def double_letters(text):
    previous = ""
    for letter in text:
        if letter == previous:
            return True
        previous = letter
    return False

print(double_letters("nono"))