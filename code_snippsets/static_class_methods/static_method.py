class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)


Person.print_type()  # Person - обращение к статическому методу через имя класса

tom = Person()
tom.print_type()  # Person - обращение к статическому методу через имя объекта