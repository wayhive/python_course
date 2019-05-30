# class Animal:
	# def __init__(self, arg1,arg2):
		# self.property = arg1
		# self.property = arg2
#changing python version from version 2 to version 3 and vice verser
# alias python=python3.7 
class Animal:
	def __init__(self,name,country):
		self.name = name
		self.country = country

	def print_details(self):
		print(self.name, self.country)

	# def print_hello(self):
	# 	print("hello","world")	

class Mammal(Animal):
	def __init__(self,name,country,age,height):
		Animal.__init__(self,age,height)
		self.name = name
		self.country = country
		self.age = age
		self.height = height

	def print_details(self):
		print(self.name, self.country,self.age, self.height)









cow = Animal('rabo','germany')
cow.print_details()
# cow.print_hello()

calf = Mammal('calpho','Kenya',5,2)
calf.print_details()

 