# Type casting refers to converting an object of one type into another.

# Python Implicit Casting - When any language compiler/interpreter automatically 
# converts object of one type into other, it is called automatic or implicit casting.

# ----------------------------------------------------------------------------------------------------

# Python Implicit Casting
# In implicit type casting, a Python object with lesser byte size is upgraded to 
# match the bigger byte size of other object in the operation.

# For example, an integer object in Python occupies 4 bytes of memory, while a float object 
# needs 8 bytes because of its fractional part. Hence, Python interpreter 
# doesn't automatically convert a float to int, because it will result in 
# loss of data. On the other hand, int can be easily converted into 
# float by setting its fractional part to 0.

# Automatic or implicit casting is limited to int to float conversion

# Example 1
a=10   # int object converted to float object 10.0
b=10.5 # float object
c=a+b
print(c) # 20.5

# Example 2
# a Boolean object is first upgraded to int and then to float, before 
# the addition with a floating point object. Please note that 
# True is equal to 1, and False is equal to 0.
a=True 
b=10.5
c=a+b
print (c) # 11.5 

# ----------------------------------------------------------------------------------------------------

# Python Explicit Casting
# You can use Python's built-in functions int(), float() and str() to perform the 
# explicit conversions such as string to integer.

a = int(10) # is same as a=10
a = int(10.5) # converts a float object to int - a=10
a = int(2*3.14) #expression results float, is converted to int - a=6
a = int(True) # Boolean to integer - a=1
a = int("15") # String to integer - a=15
a = int("10"+"01") # String concatenation to integer - a=1001
a = int("110011", 2) # Binary string to integer - a=51
a = int("20", 8) # Octal string to integer - a=16
a = int("2A9", 16) # Hexa-decimal string to integer - a=681

a = float(100) # Integer to float - a=100.0
a = float("9.99") # String to float - a=9.99
a = float("1.00E4") # scientific notations E or e to float - a=10000.0
a = float("1.00E-4") # scientific notations E or e to float - a=0.0001

a = str(10) # Integer to string - a='10'
a = str(11.10) # Float to string - a='11.1'
a = str(2/5) # Division expression to string - a='0.4'
a = str(10E4) # scientific notations E or e - a='100000.0'
a = str(1.23e-4) # scientific notations E or e - a='0.000123'
a = str('True') # Boolean to string a='True'
a = str([1,2,3]) # List to string - a='[1,2,3]'
a = str((1,2,3)) # Tuple to string - a='(1,2,3)'
a = str({1:100, 2:200, 3:300}) # Dictionary to string - a='{1:100, 2:200, 3:300}'

a = list("Hello") # String to list - a=['H', 'e', 'l', 'l', 'o']
a = list((1,2,3,4,5)) # Tuple to list - a=[1, 2, 3, 4, 5]

a = tuple("Hello") # String to tuple - a=('H', 'e', 'l', 'l', 'o')
a = tuple([1,2,3,4,5]) # List to tuple - a=(1, 2, 3, 4, 5)

# ----------------------------------------------------------------------------------------------------