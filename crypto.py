#!/usr/bin/env python

#------------------------------------------------------------------------------
# Set 1 Question 1

# Convert hexadecimal string to base64
def hexToBase64(s):

    # convert to 8-bit binary
    binary_string = hexToBinary(s)

    # convert binary string to base64
    base64_str = binaryToBase64(binary_string)

    return base64_str


# Convert a binary string to base64
def binaryToBase64(s):

    # check how many padding bits we need
    padding = len(s) % 6
    if(padding !=0):
        padding = (6 - (len(s) % 6)) / 2

    # convert to n-bit binary string to 6-bit binary
    six_bit_binary_string = padNBits(s, 6)

    # convert binary to Base64 string
    base64_str = encodeBase64(six_bit_binary_string)    

    # add padding bits
    base64_str = ''.join([base64_str, '='*padding]) 

    return base64_str


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

def hexToStr(s):

    string = ''
    for i in splitString(s,2):
        string += chr(int(i,16))
    return string

# Converts a number to a 8-bit binary number
def intToBinary(n):
    return '{0:08b}'.format(int(n))

def intTo6BitBinary(n):
    return '{0:06b}'.format(int(n))


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


def base64ToBinary(s):
    baseList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    binary_str = ''
    padding_bits = 0

    for c in s:
        if c == '=':
            padding_bits+= 2
            continue
        binary_str += intTo6BitBinary(baseList.index(c))

    # remove padding
    if(padding_bits):
        binary_str = binary_str[:-padding_bits]

    return binary_str


def strToHex(s):
    ascii_list = ''
    for c in s:
        ascii_list+=asciiToHex(ord(c))

    return ascii_list


def strToBase64(s):
    return hexToBase64(strToHex(s))


def base64ToStr(s):
    
    string = ''

    #convert to binary
    binary_str = base64ToBinary(s)

    for c in splitString(binary_str, 8):
        string += chr(binaryToAscii(c))
    
    return string

def binaryToStr(s):
    string = ''
    for c in splitString(s, 8):
        string += chr(binaryToAscii(c))
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
    ascii_numbers = binaryStrToAscii(s)
    hex_string = ''
    for i in ascii_numbers:
        hex_string += "{0:0>2x}".format(int(i))

    return hex_string 


# Convert a binary string of n-bits to a list of ascii decimal numbers
def binaryStrToAscii(s):
    ascii_list = []
    for i in splitString(s,8):
        ascii_list.append( str(binaryToAscii(i)) )
    return ascii_list  


def binaryToAscii(s):
    return int(s,2)

# Convert an ascii decimal to hexadecimal
def asciiToHex(n):
    return "{0:0>2x}".format(int(n))




#------------------------------------------------------------------------------
# Set 1 Question 3




# Return a rank value for a sentance depending on how many common words it contains
def getRank(s):
    common = ['e','t','a','o','i','n']
    less_common = ['s','h','r','d','l','u']
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'is', "I'm", 'on', 'at']
    rank = 0
    string = s.lower()
    for i in range (0, len(string)):
        if s[i] in common:
            rank += 2
        if s[i] in less_common:
            rank += 1

    for word in s.split(' '):
        if(word in common_words):
            rank += 1
    return rank


# returns the most likely decoded message and key for a hexadecimal string

def findSingleCharacterKey(s):
    a_to_z = "1234567890abcdefghijklmnopqrstuvwxyzABCDEDFGHJKLMNOPQRSTUVWXYZ:'., "
    ranked = {}
    highest_ranked = 0

    for key in a_to_z:
        
        decoded = decodeSingleCharacterKey(s, intToBinary(ord(key)))

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
    for byte in splitString(s, 8):

        # XOR each binary string against potential key
        string += fixed_xor_str(byte, key)

    # convert decoded message back to hexadecimal
    decoded = binaryToStr(string)

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



# encrypt s(string) with repeating key(string)
# returns binary string
def encryptRepeatingKeyXOR(s, key):
    
    #convert the string and key to binary
    binary_s = strToBinary(s)
    binary_keys = splitString(strToBinary(key), 8)

    encoded_string = ''
    for i, binary in enumerate(splitString(binary_s, 8)):
        encoded_string += fixed_xor_str(binary, binary_keys[i%len(key)])

    return encoded_string




#------------------------------------------------------------------------------
# Set 1 Question 6




# hamming distance of a binary string is equal to the no of 1's in s1 XOR s2 
def hamming_distance(s1, s2):
    tuplets = zip(s1, s2)
    sum_of = 0
    for ch1, ch2 in tuplets:
        sum_of += int(ch1 != ch2)

    return sum_of


def keyWithLowestVal(d):
     return min(d, key=d.get)


def findRepeatingXORKeysize(s):

    norm_edit_distances = {}
    for KEYSIZE in range(2,40):
        keysize_message = splitString(s, (KEYSIZE*8))
        total_blocks = len(keysize_message)
        distance = 0

        for i,k in zip(keysize_message[0::2], keysize_message[1::2]):
            distance +=hamming_distance(i,k)

        norm_edit_distances[KEYSIZE] = (float(distance)/float(total_blocks)) / float(KEYSIZE)

    return keyWithLowestVal(norm_edit_distances)



# decrypt a binary string encrypted with a repeating key
# returns original string
def decryptRepeatingKeyXOR(s, key):
    
    #convert key to binary
    binary_keys = splitString(strToBinary(key), 8)

    encoded_string = ''
    for i, byte in enumerate(splitString(s, 8)):
        encoded_string += fixed_xor_str(byte, binary_keys[i%len(key)])

    return binaryToStr(encoded_string)


def findRepeatingXORKey(binary_cipher):

    # calculate possible keysize
    KEYSIZE = findRepeatingXORKeysize(binary_cipher)

    # break the ciphertext into blocks of KEYSIZE length.
    keysize_blocks = splitString(binary_cipher, 8*KEYSIZE)

    transposed_blocks = []

    # Now transpose the blocks: make a block that is the first byte of every 
    # block, and a block that is the second byte of every block, and so on.
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

    return KEY




#------------------------------------------------------------------------------
# Set 1 Question 7




#------------------------------------------------------------------------------
# Set 1 Question 8




# problem with ECB is that it is stateless and deterministic; 
# the same 16 byte plaintext block will always produce the same 16 byte 
# ciphertext
def ECBScore(s):

    # NB: ideally we may want a list of all 16 byte blocks from each two byte 
    # position increment within the string. 
    
    # split string into 16 byte blocks
    blocks = splitString(s, 16)

    score = 0
    seen = set()
    for x in blocks:
        if x in seen:
            score += 1
        seen.add(x)
    return score




#------------------------------------------------------------------------------
# Set 2 Question 9




# implement PKCS#7 padding on a string s until len(s) == length
def PKCSPad(s, length):
    padded_string = s
    str_len = len(s)
    pad_bytes = length - str_len

    if (pad_bytes < 0):
        return '\nError: string is longer than provided length'


    for i in range(0,pad_bytes):
        padded_string += '\X04'

    return padded_string



