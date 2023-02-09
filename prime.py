for n in range(1,100):
	if n >=1:
		for i in range(2, int(n/2)):
			if (n % i) == 0:
				break
		else:
			print(n)

