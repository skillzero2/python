persones = {}

def add_friends(name_of_person, list_of_friends):
    a = persones.get(name_of_person)
    if a:
        persones[name_of_person] = a + list_of_friends
    else:
        persones[name_of_person] = list_of_friends

def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in persones[name_of_person1]:
        return True
    return False

def print_friends(name_of_person):
    a = reversed(persones[name_of_person])
    for i in a:
        print(i, end=' ')
    print()

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
