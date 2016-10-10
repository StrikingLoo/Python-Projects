def fib(n):
	a = 1
	b = 1
	i = 1
	while i < n:
		if i%2==0:
			b+=a
		else:
			a+=b
		i+=1
	if n%2==1:
		return a
	else:
		return b

j=1	
while j<100:
	print(str(fib(j)))
	j+=1
	
asd = input('dale gato')