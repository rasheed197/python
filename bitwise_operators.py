# Python bitwise operators are normally used to perform bitwise operations on integer-type objects.

# Bitwise operators are binary in nature, except (Not operator ~)

# The following are the bitwise operators in Python -
# 1. Bitwise AND Operator (&)
# 2. Bitwise OR Operator (|)
# 3. Bitwise XOR Operator (^)
# 4. Bitwise NOT Operator (~)
# 5. Bitwise Left Shift Operator (<<)
# 6. Biwtise Right Shift Operator (>>)

# ---------------------------------------------------------------------------------------------------------------------------

# Bitwise AND Operator (&)
# It returns True only if both the bit operands are 1 (i.e. True). 
# All the combinations are −

#   0 & 0 is 0
#   1 & 0 is 0
#   0 & 1 is 0
#   1 & 1 is 1

# When you use integers as the operands, both are converted in equivalent binary, 
# the & operation is done on corresponding bit from each number, starting from the 
# least significant bit and going towards most significant bit.

a=60
b=13
print(f"a={a}, b={b}")
print ("a&b =", a&b) # 12

# ---------------------------------------------------------------------------------------------------------------------------

# Bitwise OR Operator (|)
# If any bit operand is 1, the result is 1 otherwise it is 0.

#   0 | 0 is 0
#   0 | 1 is 1
#   1 | 0 is 1
#   1 | 1 is 1

a=60
b=13
print()
print(f"a={a}, b={b}")
print ("a|b =", a|b) # 61

# Bitwise XOR Operator (^)
# The term XOR stands for exclusive OR. 
# It means that the result of OR operation on two bits will be 1 if only one of the bits is 1.

#   0 ^ 0 is 0
#   0 ^ 1 is 1
#   1 ^ 0 is 1
#   1 ^ 1 is 0

a=60
b=13
print()
print(f"a={a}, b={b}")
print ("a^b =", a^b) # 49

# ---------------------------------------------------------------------------------------------------------------------------

# Bitwise NOT Operator (~)
# It flips each bit so that 1 is replaced by 0, and 0 by 1.
# It returns the complement of the original number.

# Python uses 2's complement method. 

# For positive integers, it is obtained simply by reversing the bits.

# For negative number, -x, it is written using the bit pattern for (x-1) with all 
# of the bits complemented (switched from 1 to 0 or 0 to 1).

# -1 is complement(1 - 1) = complement(0) = "11111111"
# -10 is complement(10 - 1) = complement(9) = complement("00001001") = "11110110"
# +10 = complement(10) = complement("00001010") = "11110101"

a=60
print()
print(f"a={a}")
print ("~a =", ~a) # 61

# ---------------------------------------------------------------------------------------------------------------------------

# Bitwise Left Shift Operator (<<)
# Shift the bits of a binary number towards the left
# As a consequence, it multiplies the number by 2 to power n
# Where "n" is the magnitude of shift

a=60
print()
print(f"a={a}")
print ("a<<2 =", a<<2) # 240 = 60 * 2 to the power 2

# How it works

# Binary equivalent 0f 60 = 0011 1100

# 0011 1100
# <<
#     2
# -------------
# 1111 0000

# ---------------------------------------------------------------------------------------------------------------------------

# Biwtise Right Shift Operator (>>)
# Shift the bits of a binary number towards the right
# As a consequence, it divides the number by 2 to power n
# Where "n" is the magnitude of shift

a=60
print()
print(f"a={a}")
print ("a>>2 =", a>>2) # 15 = 60 / 2 to the power 2

# How it works

# Binary equivalent 0f 60 = 0011 1100

# 0011 1100
#        >>
#     2
# -------------
# 0000 1111

# ---------------------------------------------------------------------------------------------------------------------------
