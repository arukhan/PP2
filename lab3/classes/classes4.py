import math
class Point:
    def __init__(self, x = int(input()), y = int(input())):
        self.x = x
        self.y = y
    def show(self):
        return "Point:({}, {})".format(self.x, self.y)
    def move(self, ax = int(input()), ay = int(input())):
        self.x += ax
        self.y += ay
        return "Moved point:({}, {})".format(self.x, self.y)
    def dist(self, secondx = int(input()), secondy = int(input())):
        subsx = self.x - secondx
        subsy = self.y - secondy
        return math.sqrt(subsx ** 2 + subsy ** 2)
p = Point()
s = p.show()
print(s)
m = p.move()
print(m)
d = p.dist()
print(d)