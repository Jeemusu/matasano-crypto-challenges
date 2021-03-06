#!/usr/bin/env python

from crypto import *
import time

#start timer
start = time.time()


"""
Problem

In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
"""


#
# Solution
#

# read message from file into list of blocks
with open ("1.8.txt", "r") as myfile:
    blocks = myfile.readlines()

# loop though each line and rank them for repeated 16 byte blocks
for lineno,line in enumerate(blocks):
    score = ECBScore(line)
    if score > 0:
        print "\nLine: %s , Rank: %s" % (lineno + 1, score)

print '-----------------------------------------------------------------------'
print "Execution time: %s" % (time.time()-start) 
print '\n'