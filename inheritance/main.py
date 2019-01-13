from rectangle import Rectangle
from triangle import Triangle

rectangle = Rectangle()
triangle = Triangle()

rectangle.set_values(20, 20)
triangle.set_values(20, 20)

rectangle.set_color('red')
triangle.set_color('blue')

print(rectangle.area())
print(triangle.area())
print(rectangle.get_color())
print(triangle.get_color())
