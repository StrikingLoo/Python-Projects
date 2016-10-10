def merge(a,b):
	i=0
	j=0
	mergearr=[]
	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			mergearr.append(a[i])
			i+=1
		else:
			mergearr.append(b[j])
			j+=1
	while i<len(a):
		mergearr.append(a[i])
		i+=1
	while j<len(b):
		mergearr.append(b[j])
		j+=1
	return mergearr

def mergesort(z):
	if len(z)==1:
		return z
	else:
		ind=(len(z)//2)
		print(str(ind))
		if len(z)==2:
			return merge(z[:ind],z[ind:])
		else:
			return merge(mergesort(z[:ind]),mergesort(z[ind:]))
	

print(mergesort([1,2,4,3,48,56986,34,454,325,65]))
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
z=input('funca o no funca macho?')