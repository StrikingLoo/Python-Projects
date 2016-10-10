class Animal():
	animals=[]
	def __init__(self,name,furScalesFeathers=0,legs=4,hasWings=0,teethBeak=0,hasTail=1,isPoisonous=0,canFly=0,mansBestFriend=0):
		self.name=name
		self.furScalesFeathers=furScalesFeathers
		self.legs=legs
		self.hasWings=hasWings
		self.teethBeak=teethBeak
		self.hasTail=hasTail
		self.isPoisonous=isPoisonous
		self.canFly=canFly
		self.mansBestFriend=mansBestFriend
		Animal.animals.append(self)
	def __str__(self):
		return self.name
	@staticmethod
	def aniList():
		listString=''
		for i in Animal.animals:
			listString+=i.name + ', '
		print listString[:-2]
	

			
			
			
def prarr(arr):
		listString=''
		for i in arr:
			listString+=i.name + ', '
		print listString[:-2]	
		
def copyArray(arr):
	nArr=[]
	for i in arr:
		nArr.append(i)
	return nArr 

def filterBy(array,prop,val=1): #deletes all animals with this val on this prop, returns new array.
		#print 'deleting all animals with the property ' +prop+ ' with a value of '+str(val)
		nAns=copyArray(array)
		i=0
		while i < len(nAns):
			if prop=='furScalesFeathers':
				if nAns[i].furScalesFeathers!=val:
					del nAns[i]
					i-=1
			if prop=='legs':
				if nAns[i].legs!=val:				
					del nAns[i]
					i-=1
			if prop=='hasWings':
				if nAns[i].hasWings!=val:				
					del nAns[i]
					i-=1
			if prop=='teethBeak':
				if nAns[i].teethBeak!=val:				
					del nAns[i]
					i-=1
			if prop=='hasTail':
				if nAns[i].hasTail!=val:				
					del nAns[i]
					i-=1
			if prop=='isPoisonous':
				if nAns[i].isPoisonous!=val:				
					del nAns[i]
					i-=1
			if prop=='canFly':
				if nAns[i].canFly!=val:				
					del nAns[i]
					i-=1
			if prop=='mansBestFriend':
				if nAns[i].mansBestFriend!=val:				
					del nAns[i]
					i-=1
			i+=1
		return nAns

cat = Animal('cat')
dog=Animal('dog',0,4,0,0,1,0,0,1)
lizard=Animal('lizard',1,4,0,0,1,0)
hen=Animal('hen',2,2,1,1,1,0,0)
eagle=Animal('eagle',2,2,1,1,1,0,1)
spider=Animal('spider',0,8,0,0,0,1,0)

print '##################################'
print 'choose one of the following animals,'
print 'the program will guess which one you chose:'
Animal.aniList() 


question={
'hasWings':'does your animal have wings?'
,'teethBeak':'does your animal have a beak? (answer no if it has teeth)'
,'hasTail':'does your animal have a tail?'
,'isPoisonous':'is your animal poisonous?'
,'canFly':"can your animal fly? (we assume hens can't)",
'mansBestFriend':"is your animal man's best friend?"
}


def booleanProperty(prop,possible,unchecked):
	hasProp=-1
	while hasProp!=1 and hasProp!=0:
		hasProp=raw_input(question[prop]+' Y/N: ')
		if hasProp=='Y':
			hasProp=1
		elif hasProp=='N':
			hasProp=0		
	possible=filterBy(possible,prop,hasProp)		
	if filterBy(possible,prop,1)==[] or filterBy(possible,prop,0)==[]:
		unchecked.remove(prop)
	return possible
			




def guessAnimal():
	possible= Animal.animals
	unchecked = ['furScalesFeathers','legs','hasWings','teethBeak','hasTail','isPoisonous','canFly','mansBestFriend']
	if (len(possible)>1):
		#prarr( possible )
		possible = booleanProperty('hasWings',possible,unchecked)
		
		if filterBy(possible,'hasWings',0)==[]:
			print "your animal has wings."
		else:
			print "your animal doesn't have wings."
	if (len(possible)>1):
		possible =  booleanProperty('hasTail',possible,unchecked)
		
		if filterBy(possible,'hasTail',0)==[]:
			print "your animal has a tail."
		else:
			print "your animal doesn't have a tail."	
	if (len(possible)>1):
		possible =  booleanProperty('teethBeak',possible,unchecked)
		if filterBy(possible,'teethBeak',1)==[]:
			print "your animal has teeth."
		else:
			print "your animal has a beak."
	if (len(possible)>1):	
		possible =  booleanProperty('isPoisonous',possible,unchecked)
		if filterBy(possible,'isPoisonous',0)==[]:
			print "your animal is poisonous."
		else:
			print "your animal is not poisonous."
	if (len(possible)>1):	
		possible =  booleanProperty('canFly',possible,unchecked)
		if filterBy(possible,'canFly',0)==[]:
			print "your animal can fly."
		else:
			print "your animal can not fly."
	if (len(possible)>1):
		possible =  booleanProperty('mansBestFriend',possible,unchecked)
		prarr(possible)
		if filterBy(possible,'mansBestFriend',0)==[]:
			print "your animal is loyal to the marrow."
		else:
			print "your animal thinks he owns you."
	
	if (len(possible)==0):
		print 'I do not know such an animal.'
	else:
		print possible[0].name + ' is your animal, right?'
		
		
	
guessAnimal()








