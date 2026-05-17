class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point(self.x + p.x, self.y + p.y)    
    
    def print_point(self):
        print(f"({self.x}, {self.y})")

    def __add__(self, p): # operator overloading
        return Point(self.x + p.x, self.y + p.y)    


p1 = Point(2, 3)
p2 = Point(5, 7)  

# p = p1.sum(p2)  # Using the sum method
p = p1 + p2  # We overloaded the + operator by defining the __add__ method
p.print_point()