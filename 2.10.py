#!/usr/bin/env python

from crypto import *
import time

#start timer
start = time.time()



"""
Problem

CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block cipher natively only transforms individual blocks.

In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.

The first plaintext block, which has no associated previous ciphertext block, is added to a "fake 0th ciphertext block" called the initialization vector, or IV.

Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise to combine them.

The file here is intelligible (somewhat) when CBC decrypted against "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

"""







#
# Solution
#

message = 'The crow flies from the chicken coop at dawn yo!'
key = 'YELLOW SUBMARINE'
iv = bytes('\x00' * 16)
#iv = bytes([0] * 16)

encrypted_message = encryptAES_CBC(message, iv, key)
print('Encrypted: %r' % encrypted_message)

# in progress
decrypted_message = decryptAES_CBC(encrypted_message, iv, key)

decryptor = AES.new(key, AES.MODE_CBC, iv)
decrypted_message = decryptor.decrypt(encrypted_message)
print('Decrypted: %r' % decrypted_message)

"""

with open ("2.10.txt", "r") as myfile:
    blocks = myfile.readlines()

# strip new lines
blocks = [x.strip('\n') for x in blocks]

# concatonate into a single string
b64_cipher =  "".join(blocks)

# decode base64
ciphertext = base64ToStr(b64_cipher)

key = 'YELLOW SUBMARINE'
IV = bytes('\x00' * 16)
decryptor = AES.new(key, AES.MODE_ECB, IV)
plain = decryptor.decrypt(ciphertext)
print plain
"""
print '-----------------------------------------------------------------------'
print "Execution time: %s" % (time.time()-start) 
print '\n'