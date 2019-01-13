import math
# class Number:
#     def __init__(self, num):
#         self.num = num

# n1 = Number(1)
# n2 = Number(2)

# n1 + n2

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, circle_obj):
        return Circle(self.__radius + circle_obj.__radius)

    def __mul__(self, circle_obj):
        return Circle(self.__radius * circle_obj.__radius)

    def __lt__(self, circle_obj):
        return self.__radius == circle_obj.__radius

    def __str__(self):
        return 'Circle area ' + str(self.area())
    
c1 = Circle(2)
c2 = Circle(3)
c3 = c1 + c2
c4 = c1 * c2
c5 = c1 == c2

print(c1.area())
print(c3.get_radius())
print(c4.get_radius())
print(c5)
print(str(c1))


