#  Bool is a sub-type of int type

# A bool object has two possible values - 
# 1. True 
# 2. False.

a=True
b=False
type(a), type(b) # (<class 'bool'>, <class 'bool'>)

# -------------------------------------------------------------------------------------------------------------------

# With True as argument, the int() function returns 1, float() returns 1.0; 
# whereas for False, they return 0 and 0.0 respectively.

a=int(True)
print ("bool to int:", a) # bool to int: 1
a=float(False)
print ("bool to float:", a) # bool to float: 0.0

# With complex(), the argument is taken as real part, setting the imaginary coefficient to 0.
a=complex(True)
print ("bool to complex:", a) # bool to complex: (1+0j)

# -------------------------------------------------------------------------------------------------------------------

# Python Boolean Expression
# Python boolean expression is an expression that evaluates to a Boolean value.
# The bool() method is used to return the truth value of an expresison.

# Check true
a = True
print(bool(a)) # True

# Check false
a = False
print(bool(a)) # False

# Check 0
a = 0.0
print(bool(a)) # False

# Check 1
a = 1.0
print(bool(a)) # True

# Check Equality
a = 5
b = 10
print(bool( a==b)) # False

# Check None
a = None
print(bool(a)) # False

# Check an empty sequence
a = ()
print(bool(a)) # False

# Check an emtpty mapping
a = {}
print(bool(a)) # False

# Check a non empty string
a = 'Tutorialspoint'
print(bool(a)) # True
