#!/usr/bin/env python

from crypto import *
import time

#start timer
start = time.time()

        
"""
Problem

There's a file here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

Write a function to compute the edit distance/Hamming distance between two 
strings. The Hamming distance is just the number of differing bits. The 
distance between:

"this is a test"

and

"wokka wokka!!!"

is 37. Make sure your code agrees before you proceed.

For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE 
worth of bytes, and find the edit distance between them. Normalize this result 
by dividing by KEYSIZE.

The KEYSIZE with the smallest normalized edit distance is probably the key. 
You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 
KEYSIZE blocks instead of 2 and average the distances.

Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

Now transpose the blocks: make a block that is the first byte of every block, 
and a block that is the second byte of every block, and so on.

Solve each block as if it was single-character XOR. You already have code 
to do this.

For each block, the single-byte XOR key that produces the best looking 
histogram is the repeating-key XOR key byte for that block. Put them together 
and you have the key.

"""


#
# Solution
#

#string_a = strToBinary('this is a test')
#string_b = strToBinary('wokka wokka!!!')
#print hamming_distance(string_a, string_b)



# read message from file into list of blocks
with open ("1.6.txt", "r") as myfile:
    blocks = myfile.readlines()

# strip new lines
blocks = [x.strip('\n') for x in blocks]

# concatonate into a single string
b64_cipher =  "".join(blocks)

# convert base64 to binary
binary_cipher = base64ToBinary(b64_cipher)

# calculate possible keysize
KEYSIZE = findRepeatingXORKeysize(binary_cipher)


# break the ciphertext into blocks of KEYSIZE length.
keysize_blocks = splitString(binary_cipher, 8*KEYSIZE)

transposed_blocks = []

# Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
for i, block in enumerate(keysize_blocks[0:-1]):
    for j, byte in enumerate(splitString(block, 8)):
        if i == 0:
            transposed_blocks.append(byte)
        else:
            transposed_blocks[j] = transposed_blocks[j] + byte

KEY = ''
for block in transposed_blocks:
    #solve each block as if it where a single key XOR
    KEY += findSingleCharacterKey(block)

print "KEY: %s" % KEY
print decryptRepeatingKeyXOR(binary_cipher, KEY)

print '-----------------------------------------------------------------------'
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'