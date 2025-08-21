'''
Create a class Student with following requirements

Two data members
age : int
name : String
Four constructors
Default constructor : Should set age to 0 and name to null
Constructor with int parameter : Should set age to the passed parameter and name to null
Constructor with String parameter : Should set name to the passed parameter and age to 0
Constructor with two parameters - int and String : Should set the age to int parameter and name to String parameter
The assignment code should only be in the 4th constructor. The top 3 constructors should use telescoping to invoke the 4th constructor.
'''


class Student:

    def __init__(self, age: int = 0, name: str = None):
        if isinstance(age, int) and isinstance(name, str):
            self.age = age
            self.name = name
        elif isinstance(age, int):
            self.age = age
            self.name = None
        elif isinstance(name, str):
            self.name = name
            self.age = None

if __name__ == '__main__':
    s1 = Student()  # Default constructor
    s2 = Student(21)  # Constructor with age
    s3 = Student(None, "Alice")  # Constructor with name
    s4 = Student(25, "Bob")  # Constructor with age and name

    print(s1.age, s1.name)  # 0 None
    print(s2.age, s2.name)  # 21 None
    print(s3.age, s3.name)  # 0 Alice
    print(s4.age, s4.name)  # 25 Bob