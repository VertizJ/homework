# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

vals = []
for thing in sys.argv[1:]:
	vals.append(float(thing))

vals.sort() # sorts the numbers 

N = len(vals)
Min = vals[0]
Max = vals[-1]
mean = sum(vals)/len(vals)# find the mean or average 

# Median
if N % 2 == 1:# this part is in case you have an even number of values
	Median = vals[N//2]
else: # this is in case you have an odd number of values
	Median = ((vals[N//2] + vals[N//2-1])/2)

#std_dev
variance = 0
for value in vals:	
	variance += (value - mean)**2/N 
	
std_dev = variance ** 0.5
	
print('Count:', N)
print('Minimum:', Min)
print('Maximum:', Max)
print('Mean', f'{mean:.3f}')
print('Std. dev:', f'{std_dev:.3f}')
print('Median', f'{Median:.3f}')

"""

python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
