# Python arithmetic operators are used to perform mathematical operations such as addition, 
# subtraction, multiplication, division, and more on numbers.

# Arithmetic operators are binary operators in the sense they operate on two operands.

#       Operator	Name	            Example
# -----------------------------------------------------------------------
#       +	        Addition	        a + b = 30
#       -	        Subtraction	        a b = -10
#       *	        Multiplication	    a * b = 200
#       /	        Division	        b / a = 2
#       %	        Modulus	            b % a = 0
#       **	        Exponent	        a**b =3**2
#       //	        Floor Division	    9//2 = 4

# ----------------------------------------------------------------------------------------------------

# Addition Operator

# Adding two integers
a=10
b=20
c=a+b
print(c) # 30

# Adding integer and float
a=10
b=20.5
c=a+b
print(c) # 30.5

# Adding float and complex number
a=10+5j
b=20.5
c=a+b
print(c) # 30.5+5j

# ----------------------------------------------------------------------------------------------------

# Subtraction Operator

# Subtracting two integers
a=10
b=20
c=b-a
print(c) # 10

# Subtracting integer and float
a=10
b=20.5
c=b-a
print(c) # 10.5

# Subtracting float and complex number
a=10+5j
b=20.5
c=b-a
print(c) # 10.5-5j

# ----------------------------------------------------------------------------------------------------

# Multiplication Operator

# Multiplying two integers
a=10
b=20
c=a*b
print(c) # 200

# Multiplying integer and float
a=10
b=20.5
c=a*b
print(c) # 205.0

# Multiplying float and complex number
a=10+5j
b=20.5
c=a*b
print(c) # 205+102.5j

# ----------------------------------------------------------------------------------------------------

# Division Operator

# Dividing two integers
a=10
b=20
c=b/a
print(c) # 2.0

# Dividing integer and float
a=10
b=20.5
c=b/a
print(c) # 2.05

# Dividing float and complex number
a=10+5j
b=20.5
c=b/a
print(c) # 1.64-0.82j

# ----------------------------------------------------------------------------------------------------

# Modulus Operator

# Modulus of two integers
a=10
b=20
c=b%a
d=a%b
print(c) # 0
print(d) # 10

# Modulus of integer and float
a=10
b=20.5
c=b%a
d=a%b
print(c) # 0.5
print(d) # 10.0

# ----------------------------------------------------------------------------------------------------

# Exponent Operator

print(0**3) # 0
print(3**0) # 1

# Exponent of two integers
a=2
b=5
c=a**b
print(c) # 32

# Exponent of integer and float
a=2.5
b=5
c=a**b
print(c) # 97.65625
d=b**a
print(d) # 55.90169943749474

# Exponent of float and complex number
a=1+2j
b=4
c=a**b
print(c) # (-7-24j)

# ----------------------------------------------------------------------------------------------------

# Floor Division Operator (Integer Division)

# If both operands are positive, floor operator returns a number with fractional part removed from it. 
# For example, the floor division of 9.8 by 2 returns 4 (pure division is 4.9, strip the fractional part, result is 4).

# But if one of the operands is negative, the result is rounded away from zero (towards negative infinity). 
# Floor division of -9.8 by 2 returns -5 (pure division is -4.9, rounded away from 0).

a=9
b=2
c=a//b
print (c) # 4

a=9
b=-2
c=a//b
print (c) # -5

# ----------------------------------------------------------------------------------------------------
