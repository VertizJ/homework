
m = 1
n = 10
k = 1

for p in range(m,n+1,k):

	#check if p is divisible by 3 
	is_div3 = False
	if p % 3 == 0: is_div3 = True
	
	# check if p is perfect square
	is_square = False
	srp = p ** 0.5
	if srp == int(srp): is_square = True
	
	# check if p is prime
	is_prime = True
	for j in range (2,p):
		if p % j == 0: 
			is_prime = False
			break
	
	#output section
	print(p, end='')
	if is_div3: print('@', end='')
	if is_square: print('#', end='')
	if is_prime: print('*', end='')
	print()
		