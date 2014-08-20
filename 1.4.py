#!/usr/bin/env python

from crypto import *
import time

#start timer
start = time.time()

"""
Problem

One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.
"""


#
# Solution
#


# Grab data from file
with open ("1.4.txt", "r") as myfile:
    lines = myfile.readlines()

for s in lines:
    s=s.strip()
    key = findSingleCharacterKey(s)
    if(key):
        print "key: %s" % key
        print "string: %s" % s
        decrypted = decodeSingleCharacterKey(hexToBinary(s), intToBinary(ord(key)))
        print "message: %s" % decrypted

print '-----------------------------------------------------------------------'
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'