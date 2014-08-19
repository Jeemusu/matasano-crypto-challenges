#!/usr/bin/env python

# Split string into list of n bits
def splitString(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


# Convert hexadecimal to raw text
def decodeHex(s):
    string = ''
    
    for i in splitString(s,2):
        string += chr( int(i,16) )

    return string


# Convert hexadecimal string to a list of ASCII indexes
def hexToAscii(s):
    ascii_list = []
    
    for i in splitString(s,2):
        ascii_list.append(str(int(i,16)))

    return ascii_list


# Converts a number to a 8-bit binary number
def intToBinary(n):
    return '{0:08b}'.format(int(n))


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

# Convert hexadecimal to base64
def hexToBase64(s):
    binary_string = ''

    # convert hexadecimal string to a list of ascii indexes 
    ascii_list = hexToAscii(s)

    # convert ascii indexes to 8bit binary numbers
    for i in ascii_list:
        binary_string += intToBinary(i)

    # convert to 6-bit binary
    binary_string = padNBits(binary_string, 6)

    # convert binary to Base64 string
    return encodeBase64(binary_string)    

# XOR two boolian numbers
def fixed_xor(a,b):
    return int(a != b)

# XOR two binary strings of equal-length buffers
def fixed_xor_str(a, b):
    binary_string_a = ''
    binary_string_b = ''
    binary_string_c = ''

    # convert hexadecimal string to a list of ascii indexes 
    ascii_list_a = hexToAscii(a)
    ascii_list_b = hexToAscii(b)

    # convert ascii indexes to 8bit binary numbers
    for i in ascii_list_a:
        binary_string_a += intToBinary(i)

    for i in ascii_list_b:
        binary_string_b += intToBinary(i)

    for i in range(0,len(binary_string_a)):
        binary_string_c += str(fixed_xor(binary_string_a[i], binary_string_b[i]))

    return binary_string_c


# Convert a binary string of n-bits to a list of ascii decimal numbers
def binaryToAscii(s, n):
    ascii_list = []
    for i in splitString(s,n):
        ascii_list.append( str(int(i,2)) )
    return ascii_list  

# Convert an ascii decimal to hexadecimal
def asciiToHex(n):
    return "{0:0>2x}".format(int(n))

# Convert 8-bit binary directly to hexadecimal
def binaryToHex(s):
    ascii_numbers = binaryToAscii(s, 8)
    hex_string = ''
    for i in ascii_numbers:
        hex_string += asciiToHex(i)
    return hex_string


