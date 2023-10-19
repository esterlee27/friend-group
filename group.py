"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connects": {
            "Zalika": "friend",
            "John": "partner",
            },
        },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "connects": {
            "Jill": "friend",
            },
        },   
    "John": {
        "age": 27,
        "job": "writer",
        "connects": {
            "Jill": "partner",
            },
        },    
    "Nash": {
        "age": 34,
        "job": "chef",
        "connects": {
            "Zalika": "landlord",
            "John": "cousin"
            },
        },
    "Ester": {
        "age": 23,
        "job": "",
        "connects": {
            "Zalika": "landlord",
            "John": "cousin"
            },
        },
    }

def forget(person1, person2):
    for key in my_group.keys():
        if key == person1:
            del my_group[key]["connects"][person2]
        elif key == person2:
            del my_group[key]["connects"][person1]


def add_person(name, age, job, relations):
    my_group[name] = {
        "age": age,
        "job": job,
        "connects": relations
    }

add_person("Frosty", 23, "", {"Zalika": "landlord", "John": "cousin"})

def average_age(group):
    total = 0
    for person in group.values():
        total += person["age"]
    return total / len(group)

print(average_age(my_group))
