# A literal is a fixed value that is directly written in the source code.

# Here 10 is a literal as numeric value representing 10, which is directly stored in memory.
x=10 # 10 is a literal

# Here, even if the expression evaluates to 20, it is not literally included in source code.
y=x*2 # x*2 is not a literal

# This is also an indirect way of instantiation and not with literal.
x = int(10) # int(10) is not a literal

# Different types of python literals
# 1. Integer Literal - 
# 2. Float Literal
# 3. Complex Literal
# 4. String Literal
# 5. List Literal
# 6. Tuple Literal
# 7. Dictionary Literal

# -------------------------------------------------------------------------------------------

# Integer literal
x = 10 # Decimal literal
y = -25 # Decimal literal
z = 0 # Decimal literal

x = 0O34 # Octal literal
print(x) # 28

x = 0X1C # Hexadecimal literal
print(x) # 28

# -------------------------------------------------------------------------------------------

# Python float literal
x = 25.55
y = 0.05
z = -12.2345

x = 1.23E5 # In scientific notation
print(x) # 123000.0

x = 1.23E-2 # In scientific notation
print(x) # 0.0123

# -------------------------------------------------------------------------------------------

# Complex literal
x = 2+3j # complex literal

# -------------------------------------------------------------------------------------------

# String literal
var1='hello'
var2="hello"
var3='''hello'''
var4="""hello"""
var5='Welcome to "Python Tutorial" from TutorialsPoint'
var6="Welcome to 'Python Tutorial' from TutorialsPoint"

# -------------------------------------------------------------------------------------------

# List literal
L1=[1,"Ravi",75.50, True]

# -------------------------------------------------------------------------------------------

# Tuple literal
T1=(1,"Ravi",75.50, True)
T1=1,"Ravi",75.50, True

# -------------------------------------------------------------------------------------------

# Dictionary literal
capitals={"USA":"New York", "France":"Paris", "Japan":"Tokyo", "India":"New Delhi"}

# -------------------------------------------------------------------------------------------
