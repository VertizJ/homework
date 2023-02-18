# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# SUM P*LogP
#P = [0.1, 0.2, 0.3, 0.4]
# H = 0
# for i in range(len(p))
# Hint: try breaking your program with erroneous input

import math
import sys

p = []
# make command lines values into list first
for vals in sys.argv[1:]:
	p.append(float(vals))
p.sort()

# now do the entropy thing
h = 0
for i in range(len(p)):
	h -= p[i] * math.log2(p[i])
print(f'{h:.3f}')




"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
