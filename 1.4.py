#!/usr/bin/env python

from crypto import *
import time

#start timer
start = time.time()

"""
Problem

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.
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