class Rectange:
	def __init__(self, height, width):
		self.__height = height
		self.__width = width

	#setter
	def set_height(self, value):
		self.__height = value

	#getter
	def get_height(self):
		return self.__height

	#setter
	def set_width(self, value):
		self.__width = value

	#getter
	def get_width(self):
		return self.__width

	#method
	def area(self):
		return self.__height * self.__width

# instances
rect1 = Rectange(20, 20)
rect2 = Rectange(40, 40)

print(rect1.area())
print(rect2.area())