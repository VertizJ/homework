# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)
import mcb185
import math
import sys

wsize = int(sys.argv[2])
ethresh = float(sys.argv[3])

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
	h = entropy([A, C, G, T])
	return h

for name, seq in mcb185.read_fasta(sys.argv[1]):
	seql = list(seq)
	for i in range(len(seq)-wsize+1):
		if seqentropy(seq[i:i+wsize]) < ethresh: seql[i] = 'N'
	seq = ''.join(seql)
print(seq)
"""



python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
