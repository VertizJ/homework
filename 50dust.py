#!/usr/bin/env python3
# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import mcb185
import math
import sys
import argparse

"""
wsize = int(sys.argv[2])
ethresh = float(sys.argv[3])
"""


parser = argparse.ArgumentParser(description= 'Nucleotide Entropy Filter')
parser.add_argument('file', type=str, metavar='<path>', help = 'fasta file')
parser.add_argument('-w', required = False, type = int, default = 11, metavar = '<int>', help = 'optional integer argument [%(default)i]')
parser.add_argument('-t', required = False, type = float, default = 1.4, metavar = '<float>', help = 'optional float argument [%(default).3f]')
parser.add_argument('-s', action = 'store_true', help = 'lowercase masking')
arg = parser.parse_args()

def entropy(vals):
	assert(math.isclose(1.0,sum(vals)))
	h = 0
	for p in vals:
		if p != 0: h -= p * math.log2(p)
	return h
	
def seqentropy(seq):
	A = seq.count('A')/len(seq)
	C = seq.count('C')/len(seq)
	T = seq.count('T')/len(seq)
	G = seq.count('G')/len(seq)
	return entropy([A, C, G, T])

file = arg.file
window = arg.w
threshhold = arg.t

for name, seq in mcb185.read_fasta(file):
	seq = seq.upper()
	seqlist = list(seq)
	for i in range(len(seq)-window+1):
		win = seq[i:i+window]
		if seqentropy(win) < arg.t:
			for k in range(i,i+arg.w):
				if arg.s:
					seqlist[k] = seq[k].lower()
				else:
					seqlist[k] = 'N'
	seq = ''.join(seqlist)
	print(f'>{name}')
	for i in range(0, len(seq),60):
		print (seq[i: i+60])
		
"""
for name, seq in mcb185.read_fasta(sys.argv[1]):
	seql = list(seq)
	for i in range(len(seq)-wsize+1):
		if seqentropy(seq[i:i+wsize]) < ethresh: seql[i] = 'N'
	seq = ''.join(seql)
print(seq)


"""


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
