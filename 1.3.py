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

def findSingleCharKey(s):
    a_to_z = 'abcdefghjklmnopqrstuvwxyzABCDEDFGHJKLMNOPQRSTUVWXYZ'
    ranked = {}

    binary_string = hexToBinary(s)

    # XOR message against each potential a-z && A-Z character
    for key in a_to_z:
        string = ''

        # XOR each 8-bit segment
        for i in splitString( binary_string, 8):

            # XOR each binary string against potential key
            string += fixed_xor_str(i, intToBinary(ord(key)))

        # convert decoded message back to hexadecimal
        decoded = decodeHex(binaryToHex(string))

        # check the rank of each potential decoded message
        rank = getRank(decoded)

        if(rank > 0):
            ranked[key] = decoded

    return ranked

message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print findSingleCharKey(message)


print '-----------------------------------------------------------------------'
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'