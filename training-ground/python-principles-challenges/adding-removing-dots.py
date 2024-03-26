def add_dots(text):
    with_dots = ""
    for letter in text:
        with_dots += letter + "."
    return with_dots[:-1]

def remove_dots(text):
    return text.replace(".", "")

print(add_dots("hallo"))
print(remove_dots(add_dots("hallo")))