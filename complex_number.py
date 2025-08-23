# Python − Complex Numbers

# A complex number consists of a real part and an imaginary part, separated by either "+" or "−".

# The real part can be any floating point (or itself a complex number) number.
# The imaginary part is also a float/complex, but multiplied by an imaginary number.

# The imaginary number "j" is defined as the square root of -1

# ----------------------------------------------------------------------------------------------------------------------------

# There are two ways to form a complex object - 
# 1. literal representation
# 3. using complex() function.

a=5+6j
print(a, type(a)) # (5+6j) <class 'complex'>

a=2.25-1.2J
print(a, type(a)) # (2.25-1.2J) <class 'complex'>

a=1.01E-2+2.2e3j
print(a, type(a)) # (0.0101+2200j) <class 'complex'>

# ----------------------------------------------------------------------------------------------------------------------------

# The complex() function receives arguments for real and imaginary part, 
# and returns the complex number.
a=complex(5.3,6)
b=complex(1.01E-2, 2.2E3)
print (f"a: {a}", type(a)) # a: (5.3+6j) <class 'complex'>
print (f"b: {b}", type(b)) # b: (0.0101+2200j) <class 'complex'>

# ----------------------------------------------------------------------------------------------------------------------------

# The complex() function argument could also be two imaginary number
a=complex(1+2j, 2-3j)
print (a, type(a)) # (4+4j) <class 'complex'>

# ----------------------------------------------------------------------------------------------------------------------------

# The complex function with only one argument means the imaginary part is zero 0
a=complex(5.3)
print (f"a: {a}", type(a)) # a: (5.3+0j) <class 'complex'>

# ----------------------------------------------------------------------------------------------------------------------------

# The complex() function can also take a string argument. But it 
# would only be one argument , not two.
a= "5.5+2.3j"
b=complex(a)
print ("Complex number:", b) # Complex number: (5.5+2.3j)

# If only the real part is provided , the imaginary part will be zero
c=complex("4.3")
print ("Complex number:", c) # Complex number: (4.3+0j)

# ----------------------------------------------------------------------------------------------------------------------------

# Get the real and imaginary part of a compex number
a=5+6j
print ("Real part:", a.real) # 5.0
print ("Coefficient of Imaginary part:", a.imag) # 6.0

# ----------------------------------------------------------------------------------------------------------------------------

# We can also get the conjugate() of a complex number
# The conjugate() returns another complex number with the sign of imaginary component reversed
a=5-2.2j
print(f"conjugate of {a} =", a.conjugate()) # conjugate of (5-2.2j) = (5+2.2j)

# ----------------------------------------------------------------------------------------------------------------------------

