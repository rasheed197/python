# Python logical operators are used to form compound Boolean expressions.

# Each operand for these logical operators is itself a Boolean expression. For example
# age > 16 and marks > 80
# percentage < 50 or attendance < 75

# Along with the keyword False, Python interprets None, numeric zero of all types, 
# and empty sequences (strings, tuples, lists), empty dictionaries, and empty sets as False. 
# All other values are treated as True.

# There are three logical operators in Python. They are 
# 1. and
# 2. or
# 3. not
# They must be in lowercase.

# ------------------------------------------------------------------------------------------------------------------

# Logical "and" Operator
# For the compound Boolean expression to be True, both the operands must be True. 
# If any or both operands evaluate to False, the expression returns False.

# The expression "x and y" first evaluates "x". If "x" is false, its value is returned; 
# otherwise, "y" is evaluated and the resulting value is returned.

#   a	    b	    a and b
# ------------------------------------------
#   F	    F	    F
#   F	    T	    F
#   T	    F	    F
#   T	    T	    T

# ------------------------------------------------------------------------------------------------------------------

# Logical "or" Operator
# The or operator returns True if any of the operands is True. For the compound Boolean 
# expression to be False, both the operands have to be False.

# The expression "x or y" first evaluates "x"; if "x" is true, its value is returned; 
# otherwise, "y" is evaluated and the resulting value is returned.

#   a	    b	    a or b
# ------------------------------------------
#   F	    F	    F
#   F	    T	    T
#   T	    F	    T
#   T	    T	    T

# ------------------------------------------------------------------------------------------------------------------

# Logical "not" Operator
# This is a unary operator. The state of Boolean operand that follows, is reversed. 
# As a result, not True becomes False and not False becomes True.

#   a	    not a
# ------------------
#   F	    T
#   T	    F

# ------------------------------------------------------------------------------------------------------------------

# Logical Operators With Boolean Conditions
x = 10
y = 20
print(f"x={x}, y={y}")
print("x > 0 and x < 10:",x > 0 and x < 10) # False
print("x > 0 and y > 10:",x > 0 and y > 10) # True
print("x > 10 or y > 10:",x > 10 or y > 10) # # True
print("x%2 == 0 and y%2 == 0:",x%2 == 0 and y%2 == 0) # # True
print ("not (x+y>15):", not (x+y)>15) # False

# ------------------------------------------------------------------------------------------------------------------

# Logical Operators With Non- Boolean Conditions
x = 10 # Evaluates to true
y = 20 # Evaluates to true
z = 0 # Evaluates to False
print()
print(f"x={x}, y={y}, z={z}") 
print("x and y:",x and y) # 20
print("x or y:",x or y) # 10
print("z or x:",z or x) # 10
print("y or z:", y or z) # 20

# ------------------------------------------------------------------------------------------------------------------

# Logical Operators With Strings and Tuples
a="Hello" # Evaluates to true
b=tuple() # Evaluates to false
print()
print(f"a={a}, b={b}")
print("a and b:",a and b) # ()
print("b or a:",b or a) # "Hello"

# ------------------------------------------------------------------------------------------------------------------

# Logical Operators To Compare Sequences (Lists)
x=[1,2,3] # Evaluates to true
y=[10,20,30] # Evaluates to true
print()
print(f"x={x}, y={y}")
print("x and y:",x and y) # [10,20,30]
print("x or y:",x or y) # [1,2,3]

# ------------------------------------------------------------------------------------------------------------------