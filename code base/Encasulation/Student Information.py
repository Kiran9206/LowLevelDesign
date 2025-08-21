'''4. Student Information
Task: Create a Student class with:
Private attributes: name, age, and marks.
Public methods to:
Set and get the student's name, age, and marks.
Add a method to calculate the grade based on marks.
Ensure marks cannot be set directly but can only be modified via the provided method (with validation if needed).'''


class Student:

    def __init__(self):
        self.__name = None
        self.__age = None
        self.__marks = 0

    # Setters

    def set_name(self, name: str) -> None:
        if isinstance(name, str) and name.strip():  # Check if name is a non-empty string
            self.__name = name
            print(f"Name has been set to {self.__name}")
        else:
            print("Please enter a valid name!")

    def set_age(self, age: int) -> None:
        if isinstance(age, int) and age > 0:
            self.__age = age
            print(f"Age has been set to {self.__age}")
        else:
            print("Invalid age! Age must be a positive integer.")

    def set_marks(self, marks: float, max_limit: int = 100) -> None:
        if isinstance(marks, (int, float)) and 0 <= marks <= max_limit:
            self.__marks = marks
            print(f"Marks have been set to {self.__marks}")
        else:
            print("Invalid marks! Marks must be a number between 0 and 100.")

    # Getters

    def get_name(self) -> str:
        return self.__name  # Returning the value instead of printing

    def get_age(self) -> int:
        return self.__age  # Returning the value instead of printing

    def get_marks(self) -> float:
        return self.__marks  # Returning the value instead of printing

    def calculate_grade(self) -> None:
        if self.__marks > 80 and self.__marks <= 100:
            print(f"Grade is A for the marks {self.__marks}")
        elif self.__marks > 60 and self.__marks <= 80:
            print(f"Grade is B for the marks {self.__marks}")
        elif self.__marks > 45 and self.__marks <= 60:
            print(f"Grade is C for the marks {self.__marks}")
        else:
            print(f"Grade is F for the marks {self.__marks}")


            