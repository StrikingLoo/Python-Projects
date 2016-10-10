#!python 
class Animal(object):
	def __init__(self,species,walkType,medium):
		self.species = species
		self.walkType=walkType
		self.medium=medium
		self.legs = 0
	def __eq__(self,other):
		return self.species == other.species
	def setLegs(self,num):
		self.legs=(num)
	def __str__(self):
		return (self.species)+' '+ self.walkType+' in the '+ self.medium

class Bird(Animal):
	def __init__(self, species):
		Animal.__init__(self,species,'flies','air')
		Animal.setLegs(self,2)
	def __str__(self):
		return 'the '+self.species+' '+self.walkType+' contracting its '+str(self.legs)+' legs.'
class Chicken(Bird):
	def __init__(self):
		Animal.__init__(self,'chicken','does not fly','air')
		Animal.setLegs(self,2)
	def __str__(self):
		return Bird.__str__(self)+" It walks instead, cuz it's a "+str(self.species)
al = Chicken()
print (al)
		
# al = Bird('albatros')
# print(al)



asd = input('asd')
