names = ["Joaquin", "AnA", "ClaudIA"]

def lower_names(names:list) -> list:
    for index, name in enumerate(names):
        names[index] = name.lower()
    return names

print(lower_names(names))