# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import random
import sys

genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])

fragment = []

for i in range(genome_size):
	fragment.append(0)
	
for j in range(read_num):
	start = random.randint(0, genome_size - read_len)
	
	for k in range(read_len):
		fragment[start + k] += 1
		
print(fragment)

# you do fragment[read_len:-read_len] so that you dont undersample the ends
mi = min(fragment[read_len:-read_len])
ma = max(fragment[read_len:-read_len])
su = sum(fragment[read_len:-read_len])/(genome_size-2*read_len)
#													^^ 2*read_len account for the ends you didnt include

print(f'{mi}, {ma}, {su:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
