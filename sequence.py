
import random

n = 10
x = .5341
seq = ''
# generate random sequence
for i in range(n):
	r = random.random()
	if r <x: seq += random.choice('CG')
	else:	seq += random.choice('AT')
	
# count letters

a = 0
c = 0
g = 0
t = 0
for nt in seq:
	if 	 nt == 'A': a += 1
	elif nt == 'C': c += 1
	elif nt == 'G': g += 1
	else: 				t += 1
print(a/len(seq), c/len(seq), g/len(seq), t/len(seq))

# k-mers
print(seq)
k = 5
for i in range(len(seq)-k +1):
	k2 = k // 2
	kmer = seq[i:i+k]
	first = kmer[:k2]
	second = kmer[-k2:]
	rc = ''
	for nt in second :
		if nt == 'A' : rc = 'T' + rc
		''
		''
	print(kmer, kmer[:k2])
	# check if palindrome
	
	print(seq[i:i+k])
	
# palindromes
test = 'ACNGT'
k2 = k // 2
print(k2)
print(test[:k2], test[-k2:])