# The membership operators in Python help us determine whether an item 
# is present in a given container type object.

# Python has two membership operators: 
# 1. in 
# 2. not in

# The 'in' Operator

# The "in" operator is used to check whether - 
# 1. a substring is present in a bigger string, 
# 2. any item is present in a list or tuple,
# 3. a sub-list or sub-tuple is included in a list or tuple.

# Membership Operator with Strings
var = "TutorialsPoint"
a = "P"
b = "tor"
c = "in"
d = "To"
print()
print (f"{a} in {var}", ":", a in var) # True
print (f"{b} in {var}", ":", b in var) # True
print (f"{c} in {var}", ":", c in var) # True
print (f"{d} in {var}", ":", d in var) # False


# The 'not in' Operator
# The "not in" operator is used to check whether a sequence with the given 
# value is not present in the object like string, list, tuple, etc.

var = "TutorialsPoint"
a = "P"
b = "tor"
c = "in"
d = "To"
print()
print (f"{a} not in {var}", a not in var) # False
print (f"{b} not in {var}", b not in var) # False
print (f"{c} not in {var}", c not in var) # False
print (f"{d} not in {var}", d not in var) # True

# Membership Operator with Lists and Tuples
var = [10,20,30,40]
a = 20
b = 10
c = a-b
d = a/2
print()
print (f"{a} in {var}", ":", a in var) # True
print (f"{b} not in {var}", ":", b not in var) # False
print (f"{c} in {var}", ":", c in var) # True
print (f"{d} not in {var}", ":", d not in var) # False

# Even if a number expressed in other formats like binary, octal or hexadecimal are 
# given the membership operators tell if it is inside the sequence.
# 0x14 = 20 in base ten
print()
print(f"0x14 in {var}:", 0x14 in [10, 20, 30, 40]) # True

# However, if you try to check if two successive numbers are present in a list or tuple, 
# the in operator returns False.
var = (10,20,30,40)
a = (10, 20)
print()
print (f"{a} in {var}:", a in var) # False

# If the list/tuple contains the successive numbers as a sequence itself, then it returns True.
var = ((10,20), (30,40))
a = (10, 20)
print()
print (f"{a} in {var}:", a in var) # True

# Membership Operator with Sets
var = {10,20,30,40}
a = 20
b = 10
print()
print (f"{a} in {var}", ":", a in var) # True
print (f"{b} not in {var}", ":", b not in var) # False

var = {(10,20),30,40}
a = (10, 20)
print()
print (f"{a} in {var}:", a in var) # True

# Membership Operator with Dictionaries
# Use of in as well as not in operators with dictionary object is allowed. 
# However, Python checks the membership only with the collection of keys and not values.

var = {1:10, 2:20, 3:30}
a = 2
b = 20
print()
print (f"{a} in {var}", ":", a in var) # True
print (f"{b} in {var}", ":", b in var) # True