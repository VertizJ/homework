# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

# make a number line going for 0---->365
# along the line you will have many '0's but then you will get a hit 
# this will change the value to 1
# if the new birthday is found on the same birthday as what you have
# previously seen you will make the program take note of it then it 
# will sort the individual value to each other
# there is a type of bucket sorting which is linear 
# first generate all the birthdays and then check them as you are 
# generating them.
import random
import sys


people = int(sys.argv[2])
days = int(sys.argv[1])
precision = 1000
same = 0
for j in range(precision):
	bdays = []
	for i in range(people):
		d = random.randint(1,days)
		if d in bdays:
			same += 1
			break
		bdays.append(d)
print(same/precision)



"""
python3 33birthday.py 365 23
0.571
"""

