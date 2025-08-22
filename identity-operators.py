# The identity operators compare the objects to determine whether they 
# share the same memory and refer to the same object type (data type).

# --------------------------------------------------------------------------------------------------------------------

# Identity vs. Equivalence:
# Identity: Two variables are identical if they refer to the exact same object in memory. 
# You can check for identity using the 'is' operator or by comparing their memory addresses using id().

# Equivalence: Two objects are equivalent if they have the same value or content. 
# For lists, this means they contain the same elements in the same order.
# You check for equivalence using the == operator.

# --------------------------------------------------------------------------------------------------------------------

# Python provided two identity operators;
# 1. 'is' Operator
# 2. 'is not' Operator

# --------------------------------------------------------------------------------------------------------------------

# Python 'is' Operator
# The 'is' operator evaluates to True if both the operand objects share the same memory location. 
# The memory location of the object can be obtained by the "id()" function. 
# If the "id()" of both variables is same, the "is" operator returns True.

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# Comparing and printing return value
print(a is c) # True
print(a is b) # false

# Printing IDs of a, b, and c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

# --------------------------------------------------------------------------------------------------------------------

# Python 'is not' Operator
# The 'is not' operator evaluates to True if both the operand objects do 
# not share the same memory location or both operands are not the same objects.

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# Comparing and printing return values
print()
print(a is not c) # False
print(a is not b) # True

# Printing IDs of a, b, and c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

# --------------------------------------------------------------------------------------------------------------------

# NOTE: 
# - List "a" and "b" contain same items. But their id() differs.

# - The list or tuple contains the memory locations of individual items only and not the items itself. 

# - Hence "a" contains the addresses of 1,2 and 3 integer objects in a certain 
# location which may be different from that of "b".

print()
print (id(a[0]), id(a[1]), id(a[2]))
print (id(b[0]), id(b[1]), id(b[2]))


# --------------------------------------------------------------------------------------------------------------------