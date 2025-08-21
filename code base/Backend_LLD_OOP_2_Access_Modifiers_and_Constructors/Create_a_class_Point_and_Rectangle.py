import copy
class Point:
    def __int__(self, x:int, y:int):
        self.x = x
        self.y = y

    def copy(self):
        return copy.deepcopy(self)

class rectangle:

    def __init__(self, topLeftX:int, topLeftY:int, bottomRightX:int, bottomRightY:int):
        self.topLeft = Point(topLeftX, topLeftY)
        self.bottomRight = Point(bottomRightX, bottomRightY)

    def __int__(self, topLeft: Point, bottomRight: Point):
        self.topLeft = topLeft.copy()
        self.bottomRight = bottomRight.copy()

