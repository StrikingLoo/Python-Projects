### little app I created to test the average damage output of a level 5 rogue,
#### a lvl4 rogue with one fighter level (here called mixed),
### and a lvl3 rogue with 2 fighter levels using the two weapon fighting style and action surge
from matplotlib import pyplot as plt
def AvgDmg(dice,kind,mod):
  #e.g. AvgDmg of 2d4 = AvgDmg(2,4,0) (no ability modifier)
	return ((float(kind+1)*dice)/2)+mod
def dmg(dice,mod):
  #for notation purposes I won't use other dice
	return AvgDmg(dice,6,mod)

def avgOut(atk,ac,hasThird,dice,mod,sneakyPlus,twf):
	total = 0
	for i in range(1,21):
		for j in range(1,21):
			for k in range(1,21):
        #were I to throw 3d20 for attacks (ignoring advantage and disadvantage,
        # though the app can be refactored to take them into account).
				if (i+atk)>ac:
					total+=dmg(dice,mod)
					if i==20:
						total+=dmg(1,0)
				if (j+atk)>ac:
					if twf:
						total+=dmg(dice,mod)
					else:
						total+=dmg(dice,0)
					if j==20:
						total+=dmg(1,0)
				if hasThird and k+atk>ac:
					if k==20:
						total+=dmg(1,0)
						# if I have third atk then I got twf 
					total+=dmg(dice,mod)
	total/=(8000) ##normalizing here.
	chanceOfNoSneak = ((float(ac-atk-1)/20)**2) ##assume first attack is always sneaky
	if hasThird:
		chanceOfNoSneak*=(float(ac-atk-1)/20)
	chanceOfSneak = 1-chanceOfNoSneak
	if chanceOfSneak<0:
		chanceOfSneak = 0
	if sneakyPlus:#adding the sneak attack
		total+=dmg(3,0)*chanceOfSneak
	else:
		total+=dmg(2,0)*chanceOfSneak

	#normalize for amount of rolls
	return total
	

def show(a):
	print str(a) ##just notation purposes again.
#ex. show(dmg(1,0)) prints 3.5 (avg result for 1d6)
#these three functions do basically the same, I just separated them into test cases for ease of using. 
#test average damage output where max AC to take into account is b, min is a.
def test2Rogue(a,b):
	#print '2 lvs of rogue'
	total=0
	for l in range(a,b+1):
		print 'ac is '+str(l)
		total+=avgOut(7,l,False,1,4,True,False)
		show(avgOut(7,l,False,1,4,True,False))
	return total/(b+1-a)

def testMix(a,b):
	print 'mix it up'
	total = 0
	for l in range(a,b+1):
		#print 'ac is '+str(l)
		#(atk,ac,hasThird,dice,mod,sneakyPlus,twf)
		total+=avgOut(6,l,False,1,3,False,True)
		#show(avgOut(3,l,False,1,3,False,True))
	return total/(b+1-a)


def testFullFighter(a,b):
	#print '2 levels of fighter'
	total = 0
	for l in range(a,b+1):
		print str(l)+':'
		#(atk,ac,hasThird,dice,mod,sneakyPlus,twf)
		total+=avgOut(6,l,True,1,3,False,True)

		show(avgOut(6,l,True,1,3,False,True))
		#'compare to full rogue'
		
	return total/(b+1-a)
def testing(a,b):
	#show(testMix(a,b))
	#show(test2Rogue(a,b))
	show(testFullFighter(a,b))
def testComparing(a,b):
	diffs = []
	fighterdmg = []
	roguedmg = []
	for l in range(a,b+1):
		print str(l)+':'
		#(atk,ac,hasThird,dice,mod,sneakyPlus,twf)
		fighterdmg.append(avgOut(6,l,True,1,3,False,True))
		roguedmg.append(avgOut(7,l,False,1,4,True,False))
		diffs.append(avgOut(6,l,True,1,3,False,True)-avgOut(7,l,False,1,4,True,False))
	plt.plot(range(a,b+1),diffs)
	#plt.plot(range(a,b+1),fighterdmg)
	#plt.plot(range(a,b+1),roguedmg)
	plt.ylabel('dif')
	plt.show()
#test2Rogue(10,20)
testComparing(10,27)
####conclusion: a lv5 rogue will make less damage than
### a lv3 rogue with 2 levels of fighter, given it will have a higher chance of netting at least one sneak attack.
###the extra chance to get a sneak attack generates more damage than the extra die in its damage
## it should still be remembered that a lv5 rogue is less squishy thanks to it's lv5 feature.
show((avgOut(4,30,False,1,4,True,False)))
