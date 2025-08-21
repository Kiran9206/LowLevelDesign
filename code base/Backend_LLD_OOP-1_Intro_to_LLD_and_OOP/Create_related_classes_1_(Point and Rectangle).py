'''
Create a class Point. It should have 2 data-members

x : int
y : int
Create a class Rectangle. It should have 3 data-members

topLeft:Point
height:int
width:int
It should have 3 methods

getArea: It should return area of rectangle as an integer
getPerimeter: It should return perimeter of rectangle as an integer
getBottomRight: It should return a Point to represent the bottom right of the Rectangle.
'''


class point:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

class rectangle:

    def __init__(self, topLeft:point, height:int, width:int):
        self.topLeft = topLeft
        self.height = height
        self.width = width

    def getArea(self)-> int:
        return self.width * self.height

    def getPerimeter(self)->int:
        return 2 * (self.height + self.width)

    def getBottomRight(self)->point:
        return point(self.topLeft.x + self.width, self.topLeft.y - self.width)


if __name__ == "__main__":
    topLeft = point(0, 0)
    rect = rectangle(topLeft, 5, 10)

    print("Area of rectangle:", rect.getArea())
    print("Perimeter of rectangle:", rect.getPerimeter())
    bottomRight = rect.getBottomRight()
    print("Bottom Right Point:", f"({bottomRight.x}, {bottomRight.y})")