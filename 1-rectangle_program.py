"""
Development steps:
- Write down the objects on paper
- Writing a class for each object
- Writing methods for each class
- Calling the classes and their methods
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
