class Shape:
    def __init__(self):
        self.ar = 0
    def area(self):
        print(self.ar)

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        self.ar = self.length ** 2
        super().area()

a = int(input())

b = Square(a)
b.area()