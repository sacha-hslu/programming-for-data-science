def online_count(statuses):
    counter = 0
    for status in statuses.values():
        if status == "online":
            counter += 1
    print(counter)
    return counter

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

online_count(statuses)