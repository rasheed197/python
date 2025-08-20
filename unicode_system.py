# Python's string type uses the Unicode Standard for representing characters.

# A character is the smallest possible component of a text. 'A', 'B', 'C', etc., are 
# all different characters. So are '' and ''

# A unicode string is a sequence of code points, which are numbers from 0 through 0x10FFFF (1,114,111 decimal).

# The rules for translating a Unicode string into a sequence of bytes are called a character encoding.

# Three types of encodings are present, 
# 1. UTF-8
# 2. UTF-16 and 
# 3. UTF-32 
# 
# UTF stands for Unicode Transformation Format.

# The str type contains Unicode characters, hence any string created using single, double 
# or the triple-quoted string syntax is stored as Unicode.

# The default encoding for Python source code is UTF-8.

# Hence, string may contain literal representation of a Unicode character (3/4) or its Unicode value (\u00BE).
var = "3/4"
print (var) # 3/4
var = "\u00BE"
print (var) # 3/4

# a string '10' is stored using the Unicode values of 1 and 0 which are \u0031 and u0030 respectively.
var = "\u0031\u0030"
print (var) # 10

# Strings display the text in a human-readable format, and bytes store the characters as binary data.

# Encoding converts data from a character string to a series of bytes.

# Decoding translates the bytes back to human-readable characters and symbols.

# It is important not to confuse these two methods. encode is a string method, 
# while decode is a method of the Python byte object.

# Convert ASCII characters into a bytes object.
# ASCII is a subset of Unicode character set.
string = "Hello"
tobytes = string.encode('utf-8') # b'Hello'
print (tobytes)
string = tobytes.decode('utf-8') 
print (string) # "Hello"

# the Rupee symbol (₹) is stored in the variable using its Unicode value. 
# We convert the string to bytes and back to str.
string = "\u20B9"
print (string) # '₹'
tobytes = string.encode('utf-8')
print (tobytes) # b'\xe2\x82\xb9'
string = tobytes.decode('utf-8')
print (string)
