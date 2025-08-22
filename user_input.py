# Python User Input Functions
# 1. The input () Function
# 2. The raw_input () Function 

# ---------------------------------------------------------------------------------------------------------------------------------

# The input() Function

# When the interpreter encounters input() function, it waits for the user to 
# enter data from the standard input stream (keyboard) till the Enter key is pressed.

name = input("Enter your name : ")
city = input("Enter your city : ")

print ("Hello My name is", name)
print ("I am from ", city)

# ---------------------------------------------------------------------------------------------------------------------------------

# The raw_input() Function

# The raw_input() function works similar to input() function.
# Here only point is that this function was available in Python 2.7, 
# and it has been renamed to input() in Python 3.6

# ---------------------------------------------------------------------------------------------------------------------------------

# Taking Numeric Input in Python

# Python always read the user input as a string.
# Hence you cannot perform perform numeric operations with the input

# To overcome this problem, we shall use int() or float() method
# The int() method converts a string object to an integer.
# The float() method converts a string object into a float object.

width = int(input("Enter width : "))
height = float(input("Enter height : "))

area = width*height
print ("Area of rectangle = ", area)

# ---------------------------------------------------------------------------------------------------------------------------------

