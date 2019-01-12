# private var uses __<name> syntax
class Hello: 
	def __init__(self):
		self.a = 10
		self._b = 20
		self.__c = 30


hello = Hello()

print(hello.a)
print(hello._b)