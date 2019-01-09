class Car:
	name = "None"
	height = 10000
	speed = 200.00

	def __init__ (self, name, height):
		self.name = name 
		self.height = height
		print (self.name, " has weight", self.height)

	def set (self, name, height, speed):
		self.name = name 
		self.height = height
		self.speed = speed

class Truck (Car):
	wheels = 8

	def __init__(self):
		pass

man = Truck ()
man.wheels = 12
man.set ("Man", 16000, 120.5)
print (man.height)

audi = Car ("Audi", 2300)
audi.set ("Audi", 1450, 320.30)
print (audi.height)

subaru = Car ("Subaru", 1350)
subaru.set ("Subaru", 1350, 280.8)
print (subaru.name)