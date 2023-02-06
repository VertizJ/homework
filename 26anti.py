# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
rc = ''
for nt in dna:
	if   nt == 'A': rc = 'T' + rc
	elif nt == 'C': rc = 'G' + rc
	elif nt == 'G': rc = 'C' + rc
	else		  : rc = 'A' + rc

print(rc)




"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
