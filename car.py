class Car:
	# init method
	def __init__(self, speed, color):
		self.__speed = speed
		self.__color = color

	#setter
	def set_speed(self, value):
		self.__speed = value

	#getter
	def get_speed(self):
		return self.__speed

	#setter
	def set_color(self, value):
		self.__color = value

	#getter
	def get_color(self):
		return self.__color

# instances of the class Car
ford = Car(300, 'red')
honda = Car(250, 'blue')
audi = Car(220, 'black')

# change data
ford.set_speed(200)

print(ford.get_speed())
print(ford.get_color())