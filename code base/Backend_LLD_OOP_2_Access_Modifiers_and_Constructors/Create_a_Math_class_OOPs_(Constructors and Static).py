'''
Problem Description

Create a class Math with following requirements
- A class level data member called PI set to 3.14.
- A class level public method called getCircleArea, which takes as input an integer parameter called radius. This function should return area of the circle as a double
'''

class Math:


    PI = 3.4 #Class level member

    @classmethod
    def getCircleArea(cls, radius: int) -> float:
        return cls.PI * radius * radius

if __name__ == "__main__":
    radius = 5
    print(f"radius: {Math.getCircleArea(radius)}")


