'''
Create a Student class satisfying following requirements

It should have two data members:
age: int
name: String
It should have a display method
Signature : void:display()
It should print : “My name is <name>. I am <age> years old”
It should have a sayHello method
Signature : void:sayHello(String)
It should print : “<name data member> says hello to <name parameter>”
'''


class student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"My name is {self.name}. I am {self.age} years old")

    def sayHello(self, name):
        print(f"{self.name} says hello to {name}")

if __name__ == '__main__':
    student = student("kiran", 20)
    student.display()
    student.sayHello("Kumar")

