class Person:
    type = "Person"
    description = "Describes a person"


print(Person.type)  # Person
print(Person.description)  # Describes a person

Person.type = "Class Person"
print(Person.type)  # Class Person