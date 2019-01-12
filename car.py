# Empty Class / pass keyword
class Car:
	pass

# instances of the class Car
ford = Car()
honda = Car()
audi = Car()

# associate the data
ford.speed = 200
honda.speed = 220
audi.speed = 250

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'

ford.speed = 300
ford.color = 'blue'

print(ford.speed)
print(audi.color)