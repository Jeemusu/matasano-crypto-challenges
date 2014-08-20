#!/usr/bin/env python

from crypto import *
import time

#start timer
start = time.time()

"""
Problem

Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965

... should produce:

746865206b696420646f6e277420706c6179
"""


#
# Solution
#

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'
c = fixed_xor_hex(a, b)

print c


print '-----------------------------------------------------------------------'
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'