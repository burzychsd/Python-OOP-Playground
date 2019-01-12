class Polygon:
	__width = None
	__height = None

	#setter
	def set_values(self, width, height):
		self.__width = width
		self.__height = height

	#getters
	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

class Rectangle(Polygon):
	def area(self):
		return self.get_width() * self.get_height()

class Triangle(Polygon):
	def area(self):
		return self.get_width() * self.get_height() / 2

rect = Rectangle()
tri = Triangle()

rect.set_values(20, 20)
tri.set_values(20, 20)

print(rect.area())
print(tri.area())