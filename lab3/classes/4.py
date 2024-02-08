from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f'{self.x}, {self.y}')

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def distance(self):
        self.ams = sqrt((self.x - x1)**2 + (self.y - y1)**2)
        print(f'{float(self.ams)}')        

x1 = int(input())
y1 = int(input())
show1 = Point(x1, y1)
show1.show()

dx = int(input())
dy = int(input())
show1.move(dx, dy)
show1.show()

show1.distance()