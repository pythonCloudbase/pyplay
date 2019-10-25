class Person:
    name = "unassigned"
    def __init__(self, name):
        name = name
        self.name = "Aprisyta"


jeff = Person("jeff")
print(jeff.name, Person.name)