import numpy as np

class Shape(object):
	def __init__(self,area,perimeter,name):
		self.area=area
		self.perimeter=perimeter
		self.name=name
	def __eq__(self,other):
		return (self.name=other.name and self.area=other.area)
	def __str__(self):
		return 'a ' + self.name+' with an area of ' +str(self.area)+' and a perimeter of '+str(self.perimeter)'.'
	def __cmp__(self,other):
		return (self.area > other.area)

class Triangle(Shape):
	def __init__(self,base,height, perimeter):
		Shape.__init__(self,(base*height/2),perimeter,'triangle')
		
class Square(Shape):
	def __init__(self,side):
		Shape.__init__(self,side*side,4*side,'Square')
	def __str__(self):
		return 'a square with a '+str(side)+' long side'

class Circle(Shape):
	def __init__(self,radius):
		Shape.__init__(self,radius*radius*np.pi,2*radius*np.pi,'Circle')
	def __str__(self):
		return (Shape.__str__(self))+' It has a radius of ' + str(radius)'.'
		
