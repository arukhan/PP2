class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0    

class Square(Shape):
    def __init__(self):
        self.length = float(input())
    def area(self): 
        return self.length * self.length
    
    
x=Shape()
print(f"Area of Shape: {x.area()}")

y = Square()
print(f"Area of Rectangle: {y.area()}")

