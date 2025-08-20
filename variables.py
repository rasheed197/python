# Python variables are container for storing data values

# Create a variable
age = 18 
first_name = "rasheed"
last_name = "tiamiyu"

# Get the address where the variabe is stored
id(age)
id(first_name)

# print variable
print(age)
print(first_name)

# Delete variable
del age, first_name

# print variable types
print(type(age))
print(type(last_name))

# Casting variable types (Specify the type of a variable)
x = str(10) # '10'
y = int(10) # 10
z = float(10) # 10.0
print(x, y, z)

# Multiple variable assignment
a=b=c=10
print(a, b, c)

a,b,c=1,2,30
print(a, b, c)

a,b,c=1,2,"zara ali"
print(a, b, c)

# Check if two variables have the same id() value
a=b=10
a is b # True
print(id(a), id(b))