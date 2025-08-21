# create a default constructor and parameterised constructor


class constructor:


    def __init__(self, name=None, age=None):
        if name is not None or age is not None:
            self.name = name
            self.age = age
        else:
            self.name = "Default Name"
            self.age = 0

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


c = constructor(name="kiran")
c.display()

c1 = c
c1.name = "kiran1"
c1.display()
c.display()


