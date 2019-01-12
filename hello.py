# private var uses __<name> syntax
class Hello: 
	def __init__(self):
		self.a = 10
		self._b = 20
		self.__c = 30s

	def public_method(self):
		print(self.a)
		print(self.__c)
		print('public')
		self.__private_method()

	#private method
	def __private_method(self):
		print('private')


hello = Hello()

print(hello.a)
print(hello._b)
hello.public_method()