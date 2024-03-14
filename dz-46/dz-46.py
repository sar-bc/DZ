class Person:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
	
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self, name):
		if isinstance(name, str):
			self.__name = name
		else:
			print("Имя может быть только строковым значением")	
		
	@name.deleter
	def name(self):
		del self.__name

	@property
	def age(self):
		return self.__age
		
	@age.setter
	def age(self, age):
		if isinstance(age, int):
			self.__age = age
		else:
			print("Возраст может быть только числовым")
		
	@age.deleter
	def age(self):
		del self.__age
		
																																								
p1 = Person("Viktor", 39)
print(p1.__dict__)
print(p1.name)
p1.name = 67
print(p1.name)
print(p1.__dict__)
print(p1.age)
p1.age="asd"
print(p1.__dict__)
del p1.name
print(p1.__dict__)
								
