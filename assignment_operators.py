# The = (equal to) symbol is defined as assignment operator in Python.

# It should be noted that the = symbol is an assignment operator here 
# and not used to show the equality of LHS and RHS.

# Example 
a = 10 # assign the value 10 to the variable - a
b = 5 # assign the value 10 to the variable - b
a = a + b # assign the value of the expression a+b to the variable - a

# ----------------------------------------------------------------------------------------------------

# Cumulative or Augmented Assignment Operators

# The following are the augmented assignment operators in Python 
# 1. Augmented Addition Operator (+=)
# 2. Augmented Subtraction Operator (-=)
# 3. Augmented Multiplication Operator (*=)
# 4. Augmented Division Operator (/=)
# 5. Augmented Modulus Operator (%=)
# 6. Augmented Exponent Operator (**=)
# 7. Augmented Floor division Operator (//=)

# ----------------------------------------------------------------------------------------------------

# Augmented Addition Operator (+=)
# Supported for integer, float and complex number
a = 10
b = 5 
a += b # equivalent to a=a+b
print(a) # 15

# ----------------------------------------------------------------------------------------------------

# Augmented Subtraction Operator (-=)
# Supported for integer, float and complex number
a = 10
b = 5.5
a -= b # equivalent to a=a-b 
print(a) # 4.5

# ----------------------------------------------------------------------------------------------------

# Augmented Multiplication Operator (*=)
# Supported for integer, float and complex number 
a = 6 + 4j
b = 3 + 2j
a *= b # equivalent to a=a*b 
print(a) # 10 + 24j

# ----------------------------------------------------------------------------------------------------

# Augmented Division Operator (/=)
# Supported for integer, float and complex number 
a = 10
b = 5 
a /= b # equivalent to a=a/b
print(a) # 2.0 

# ----------------------------------------------------------------------------------------------------

# Augmented Modulus Operator (%=)
# Supported for integer and float. Not supported for complex number 
a = 10
b = 5.5
a %= b # equivalent to a=a%b 
print(a) # 4.5

# ----------------------------------------------------------------------------------------------------

# Augmented Exponent Operator (**=)
# Supported for integer, float and complex number 
a = 6 + 4j
b = 3 + 2j
a **= b # equivalent to a=a**b 
print(a) # (97.52306038414744-62.22529992036203j)

# ----------------------------------------------------------------------------------------------------

# Augmented Floor division Operator (//=)
# Supported for integer and float. Not supported for complex number 
a = 10
b = 5.5
a %= b # equivalent to a=a//b 
print(a) # 1.0

# ----------------------------------------------------------------------------------------------------