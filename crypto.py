#!/usr/bin/env python

#------------------------------------------------------------------------------
# Set 1 Question 1




# Convert hexadecimal string to base64
def hexToBase64(s):

    binary_string = hexToBinary(s)

    # convert to 6-bit binary
    binary_string = padNBits(binary_string, 6)

    # convert binary to Base64 string
    return encodeBase64(binary_string)    


def hexToBinary(s):
    binary_string = ''

    # convert hexadecimal string to a list of ascii indexes 
    ascii_list = hexToAscii(s)

    # convert ascii indexes to 8bit binary numbers
    for i in ascii_list:
        binary_string += intToBinary(i)

    return binary_string


# Convert hexadecimal string to a list of ASCII indexes
def hexToAscii(s):
    ascii_list = []
    
    for i in splitString(s,2):
        ascii_list.append(str(int(i,16)))

    return ascii_list


# Converts a number to a 8-bit binary number
def intToBinary(n):
    return '{0:08b}'.format(int(n))


# Split string into list of n bits
def splitString(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


# Pad a string with n ammount of characters c
def padNChars(s, n, c):
    return s + c * n


# Pad a string to n bits
def padNBits(s,n):

    # test if needs padding
    if(len(s) % n == 0):
        return s

    # pad string
    s = padNChars(s, (((len(s) / n) + 1) * n) - len(s), '0')

    return s


# Convert a 6-bit binary string to base64
def encodeBase64(s):
    baseList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64_string = ''

    for i in splitString(s,6):
        base64_string += baseList[int(i, 2)]

    return base64_string




#------------------------------------------------------------------------------
# Other functions




# Convert hexadecimal to raw text
def decodeHex(s):
    string = ''
    
    for i in splitString(s,2):
        string += chr( int(i,16) )

    return string




#------------------------------------------------------------------------------
# Set 1 Question 2



       
# XOR two hex strings of equal-length buffers
# returns hexadecimal
def fixed_xor_hex(a, b):
    binary_a = ''
    binary_b = ''
    binary_c = ''

    # convert hexadecimal string to a list of ascii indexes
    ascii_list_a = hexToAscii(a)
    ascii_list_b = hexToAscii(b)

    # convert ascii indexes to 8bit binary numbers
    for i in ascii_list_a:
        binary_a += intToBinary(i)

    for i in ascii_list_b:
        binary_b += intToBinary(i)

    # XOR both binary strings to get result
    binary_c = fixed_xor_str(binary_a, binary_b)

    return binaryToHex(binary_c)


# XOR two boolians
def fixed_xor(a,b):
    return int(a != b)


# XOR two binary strings of equal-length buffers
def fixed_xor_str(a, b):
    c = ''

    for i in range(0,len(a)):
        c += str(fixed_xor(a[i], b[i]))

    return c


# Convert an 8-bit binary string to hexadecimal
def binaryToHex(s):
    ascii_numbers = binaryToAscii(s, 8)
    hex_string = ''
    for i in ascii_numbers:
        hex_string += asciiToHex(i)
    return hex_string


# Convert a binary string of n-bits to a list of ascii decimal numbers
def binaryToAscii(s, n):
    ascii_list = []
    for i in splitString(s,n):
        ascii_list.append( str(int(i,2)) )
    return ascii_list  


# Convert an ascii decimal to hexadecimal
def asciiToHex(n):
    return "{0:0>2x}".format(int(n))




#------------------------------------------------------------------------------
# Set 1 Question 3




# Return a rank value for a sentance depending on how many common words it contains
def getRank(s):
    rank = 0
    common_words = ['the', 'of', 'or', 'and', 'is']
    ranked_list = {}

    # split string into words
    for word in s.split(' '):
        if(word in common_words):
            rank += 1

    return rank


# returns the most likely decoded message and key for a hexadecimal string
def findSingleCharacterKey(s):
    a_to_z = '1234567890abcdefghjklmnopqrstuvwxyzABCDEDFGHJKLMNOPQRSTUVWXYZ'
    ranked = {}
    highest_ranked = 0

    binary_string = hexToBinary(s)

    # XOR message against each potential a-z && A-Z character
    for key in a_to_z:

        decoded = decodeSingleCharacterKey(binary_string, intToBinary(ord(key)))
        # check the rank of each potential decoded message
        rank = getRank(decoded)

        if(rank > 0 and rank > highest_ranked):
            ranked = key
            highest_ranked = rank

    if ranked:
        return ranked


# XORS a 8-bit binary string against a larger binary string
def decodeSingleCharacterKey(s, key):
    string = ''

    # XOR each 8-bit segment
    for i in splitString( s, 8):

        # XOR each binary string against potential key
        string += fixed_xor_str(i, key)

    # convert decoded message back to hexadecimal
    decoded = decodeHex(binaryToHex(string))

    return decoded




#------------------------------------------------------------------------------
# Set 1 Question 4




def strToBinary(s):
    binary_str = ''
    for c in s:
        binary_str += charToBinary(c)
    return binary_str

def charToBinary(c):
    return intToBinary(ord(c))




#------------------------------------------------------------------------------
# Set 1 Question 5




def encryptRepeatingKeyXOR(s, key):
    
    #convert the string and key to binary
    binary_s = strToBinary(s)
    binary_keys = splitString(strToBinary(key), 8)

    encoded_string = ''
    for i, binary in enumerate(splitString(binary_s, 8)):
        encoded_string += fixed_xor_str(binary, binary_keys[i%len(key)])

    return binaryToHex(encoded_string)




#------------------------------------------------------------------------------
# Set 1 Question 6




