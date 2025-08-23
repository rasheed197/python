# Python − Floating Point Numbers

# A floating point number has an integer part and a fractional part, 
# separated by a decimal point symbol (.).

# ----------------------------------------------------------------------------------------------------------------------------

# There are three ways to form a float object - 
# 1. literal representation
# 2. result of an expression
# 3. using float() function.

a = 0.999 # literal representation
b = -9.99 # literal representation

c = a / b # expression evaluating to a float

d = float() # using float() function.
e = float("100") # using float() function.

print ("a:", a, "type:", type(a))
print ("c:", c, "type:", type(c))

print ("d:", d, "type:", type(d)) # 0.0
print ("e:", e, "type:", type(e))
print()

# ----------------------------------------------------------------------------------------------------------------------------

# The E or e symbol is used to shorten how many digits after the decimal point.
# E stands for Ten raised to. For example, 
# E4 is 10 raised to 4 (or 4th power of 10)

a=1E10
print("a =", a) # 10000000000.0

b=9.90E-5
print("b =", b) # 9.9e-05

c = 1.23E3
print("c =", c) # 1230.0

# ----------------------------------------------------------------------------------------------------------------------------

# Even if the integer is expressed in binary, octal or hexadecimal, the 
# float() function returns a float with fractional part as 0.
a=float(0b10)
b=float(0O10)
c=float(0xA)

print (a,b,c, sep=",") # 2.0,8.0,10.0

# ----------------------------------------------------------------------------------------------------------------------------

# A very large number with 400th power of 10 is represented by Inf. 
# If you use "Infinity" as argument for float() function, it returns Inf.
a=1.00E400
print (a, type(a)) # inf <class 'float'>
a=float("Infinity")
print (a, type(a)) # inf <class 'float'>

# ----------------------------------------------------------------------------------------------------------------------------

# Nan (stands for Not a Number). It represents any value that is undefined or not representable.
a=float('Nan')
print("a =", a)

# ----------------------------------------------------------------------------------------------------------------------------

