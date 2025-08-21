'''
Math Class
Problem Statement
You are tasked with creating a Python class for mathematical operations related to circles. The class should encapsulate the functionality required for computing the area of a circle.

Requirements
The Math class should have the following:

PI: denoting the value of PI(3.14)
getCircleArea(radius): This method should take the radius of a circle as a parameter and return the area of the circle.
Instructions
Implement the getCircleArea function in the Math class.
The getCircleArea method should properly calculate the area of a circle using the provided radius and the value of PI (Math.PI).
'''

class Math:


    PI = 3.4 #Class level member

    @classmethod
    def getCircleArea(cls, radius: int) -> float:
        return cls.PI * radius * radius

if __name__ == "__main__":
    radius = 5
    print(f"radius: {Math.getCircleArea(radius)}")