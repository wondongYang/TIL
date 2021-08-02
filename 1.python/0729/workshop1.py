# 도형 만들기

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():

    def __init__(self, x, y): # => 오류발생 어떤 변수를 넣어야할지 모르겠음
        super().__init__(x, y) # => 오류발생 어떤 변수를 넣어야할지 모르겠음
        
    def get_area(self, other):
        return abs(self.x - other.x) * abs(self.y - other.y)

    def get_perimeter(self, other):
        return 2 * (abs(self.x - other.x) + abs(self.y - other.y))

    def is_square(self, other):
        if abs(self.x - other.x) == abs(self.y - other.y):
            return True
        else:
            return False 

    
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_are())
print(r2.get_perimeter())
print(r2.is_square())