class Shape:
    def __init__(self):
        self.ar = 0
    def area(self):
        print(self.ar)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        self.ar = self.length * self.width
        super().area()

a = int(input())
b = int(input())

ans = Rectangle(a, b)
ans.area()