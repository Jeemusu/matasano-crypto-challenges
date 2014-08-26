#!/usr/bin/env python

from crypto import *
import time

# using PyCrypto
from Crypto.Cipher import AES

#start timer
start = time.time()

        
"""
Problem

The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".

(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
"""


#
# Solution
#

# read message from file into list of blocks
with open ("1.7.txt", "r") as myfile:
    blocks = myfile.readlines()

# strip new lines
blocks = [x.strip('\n') for x in blocks]

# concatonate into a single string
b64_cipher =  "".join(blocks)

# decode base64
ciphertext = base64ToStr(b64_cipher)

key = 'YELLOW SUBMARINE'
decryptor = AES.new(key, AES.MODE_ECB)
plain = decryptor.decrypt(ciphertext)
print plain

print '-----------------------------------------------------------------------'
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'