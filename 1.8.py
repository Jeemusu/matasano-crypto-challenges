#!/usr/bin/env python

from crypto import *
import time

# using PyCrypto
from Crypto.Cipher import AES

#start timer
start = time.time()

import itertools
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

for lineno,line in enumerate(blocks):
    if ECBScore(line) > 0:
        print(lineno + 1)


print '-----------------------------------------------------------------------'
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'