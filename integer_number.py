# Python − Integer Numbers

# An integer can be zero, positive or a negative whole number. For example, 0, 10, -5
# 10.0 is not an integer even though its fractional part is zero.

# There are three ways to form an integer object - 
# 1. literal representation
# 2. any expression evaluating to an integer
# 3. using int() function.

a = 10 # literal representation
b = 20 # literal representation

c = a + b # expression evaluating to an integer

d = int(10.5) # using int() function.
e = int("100") # using int() function.

print ("a:", a, "type:", type(a))
print ("c:", c, "type:", type(c))

print ("d:", d, "type:", type(d))
print ("e:", e, "type:", type(e))
print()

# ----------------------------------------------------------------------------------------------------------------------------

# An integer can be represented as -
# 1. Binary Number
# 2. Octal Number
# 3. Hexadecimal Number

# ----------------------------------------------------------------------------------------------------------------------------

# Binary Numbers in Python
# A number consisting of only the binary digits (1 and 0) and prefixed with "0b" is a binary number.

# If you assign a binary number to a variable, it still is an int variable.

a=0b101
print ("a:",a, "type:",type(a)) # a: 5 type: <class 'int'> 

# convert a Binary string to integer, set the base to 2 in the int() function.
b=int("0b101011", 2)
print ("b:",b, "type:",type(b)) # b: 43 type: <class 'int'>

# Use the bin() function to obtain the binary string for an integer.
a=43
b=bin(a)
print ("Integer:",a, "Binary equivalent:",b) # Integer: 43 Binary equivalent: 0b101011
print ("b:",b, "type:",type(b)) # b: 0b101011 type: <class 'str'>
print()

# ----------------------------------------------------------------------------------------------------------------------------

# Octal Numbers in Python
# An octal number is made up of digits 0 to 7 only. And prefixed with "0o" or "0O"
a=0O107
print (a, type(a)) # 71 <class 'int'>

# covert an octal string to integer, set the base to 8 in the int() function.
a=int('20',8)
print (a, type(a)) # 16 <class 'int'>

# Use the oct() function to obtain the octal string for an integer.
a=oct(71)
print (a, type(a)) # 0o107 <class 'str'>
print()

# ----------------------------------------------------------------------------------------------------------------------------

# Hexa-decimal Numbers in Python
# There are 16 symbols in the Hexadecimal number system. And prefixed with "0x" or "0X"
# They are 0-9 and A to F. 

# The first 10 digits are same as decimal digits. 
# The alphabets A, B, C, D, E and F are equivalents of 11, 12, 13, 14, 15, and 16 respectively. 
# Upper or lower cases may be used for these letter symbols.

a=0XA2
print (a, type(a)) # 162 <class 'int'>

# convert a Hexadecimal string to integer, set the base to 16 in the int() function.
a=int('0X1e', 16)
print (a, type(a)) # 30 <class 'int'>

num_string = "A1"
number = int(num_string, 16)
print ("Hexadecimal:", num_string, "Integer:",number) # Hexadecimal: A1 Integer: 161

# Use the hex() function to obtain the hexadecimal string for an integer.
a=hex(161)
print (a, type(a)) # 0xa1 <class 'str'>

# ----------------------------------------------------------------------------------------------------------------------------

# When performing arithmetic operation, the representation doesn't matter.
# Internally, they are all integers

a=10 #decimal
b=0b10 #binary
c=0O10 #octal
d=0XA #Hexadecimal
e=a+b+c+d

print ("addition:", e) # addition: 30
print()

# ----------------------------------------------------------------------------------------------------------------------------

