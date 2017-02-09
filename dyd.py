### little app I created to test the average damage output of a level 5 rogue,
#### a lvl4 rogue with one fighter level (here called mixed),
### and a lvl3 rogue with 2 fighter levels using the two weapon fighting style and action surge

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
	if sneakyPlus:#adding the sneak attack
		total+=dmg(3,0)
	else:
		total+=dmg(2,0)

	#normalize for amount of rolls
	return total
	

def show(a):
	print str(a) ##just notation purposes again.
#ex. show(dmg(1,0)) prints 3.5 (avg result for 1d6)
#these three functions do basically the same, I just separated them into test cases for ease of using. 
#test average damage output where max AC to take into account is b, min is a.
def test2Rogue(a,b):
	print '2 lvs of rogue'
	total=0
	for l in range(a,b+1):
		#print 'ac is '+str(l)
		total+=avgOut(4,l,False,1,4,True,False)
		#show(avgOut(4,l,False,1,4,True,False))
	return total/(b+1-a)

def testMix(a,b):
	print 'mix it up'
	total = 0
	for l in range(a,b+1):
		#print 'ac is '+str(l)
		#(atk,ac,hasThird,dice,mod,sneakyPlus,twf)
		total+=avgOut(3,l,False,1,3,False,True)
		#show(avgOut(3,l,False,1,3,False,True))
	return total/(b+1-a)


def testFullFighter(a,b):
	print '2 levels of fighter'
	total = 0
	for l in range(a,b+1):
		#print 'ac is '+str(l)
		#(atk,ac,hasThird,dice,mod,sneakyPlus,twf)
		total+=avgOut(3,l,True,1,3,False,True)
		#show(avgOut(3,l,True,1,3,False,True))
		#'compare to full rogue'
		#show(avgOut(4,l,False,1,4,True,False))
	return total/(b+1-a)
def testing(a,b):
	#show(testMix(a,b))
	show(test2Rogue(a,b))
	show(testFullFighter(a,b))

#testFullFighter(10,20)
testing(12,12)
####conclusion: a lv5 rogue will make more damage than
### a lv3 rogue with 2 levels of fighter provided the enemies have an 
## AC of 14 or higher. given an enemy of AC 12 or 13 damage is comparable (avg difference of 1)
## especially since I did not take into account critical sneak attacks,
## it is therefore, taking into account the cool lv5 feature, convenient to become a lv5 rogue, 
###from a purely munchkin perspective. 
