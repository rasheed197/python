#  The Comparison Operators are also called Relational Operators.

# Comparison operators in Python are very important in Python's conditional 
# statements (if, else and elif) and looping statements (while and for loops).

# Comparison operators are binary in nature, requiring two operands.

# An expression involving a comparison operator is called a Boolean expression, 
# and always returns either True or False.

#       Operator    Name                        Example
# --------------------------------------------------------------------
#       <	        Less than	                a<b
#       >	        Greater than	            a>b
#       <=	        Less than or equal to	    a<=b
#       >=	        Greater than or equal to	a>=b
#       ==	        Is equal to	                a==b
#       !=	        Is not equal to	            a!=b

# comparison operators with integer numbers 
a=5
b=7
print (a>b) # False
print (a<b) # True

# comparison operators with an integer and float 
a=10
b=10.0
print (a>b) # False
print (a<b) # False
print (a==b) # True
print (a!=b) # False

# comparison operators with complex numbers 
# complex number do not support < and > operator
a=10+1j
b=10.-1j
print (a==b) # False
print (a!=b) # True

# comparison of booleans
# Boolean objects in Python are really integers: True is 1 and False is 0.
# In fact, Python treats any non-zero number as True.
a=True
b=False
print (a>b) # True
print (a<b) # False
print (a==b) # False
print (a!=b) # True

# comparison of sequence types
# In Python, comparison of only similar sequence objects can be performed.
# A list cannot be compared with a tuple, even if both have same items.

# comparison of strings
a='BAT'
b='BALL'
print (a>b) # True - T > L
print (a<b) # False
print (a==b) # False
print (a!=b) # True

# comparison of tuples
a=(1,2,4)
b=(1,2,3)
print (a>b) # True - 4 > 3
print (a<b) # False
print (a==b) # False
print (a!=b) # True

# comparison of dictionary object
# Dictionary object do not support < and > operator
a={1:1, 2:2, 3:3}
b={3:3, 1:1, 2:2}
print (a==b) # True
print (a!=b) # False



