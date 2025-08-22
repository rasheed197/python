# The print() function is used to display values of Python expression given in 
# parenthesis, on Python's console, or standard output (sys.stdout).

print ("Hello World ")

# ---------------------------------------------------------------------------------------------------------------------------------

# Any number of Python expressions can be there inside the parenthesis.
# They must be separated by comma symbol.

a = "Hello World"
b = 100
c = 25.50
d = 5+6j
print ("Message: a")
print (b, c, b-c)
print(pow(100, 0.5), pow(c,2))

# ---------------------------------------------------------------------------------------------------------------------------------

# If the print() function contains more than one expressions inside the parenthesis
# the values are separated by a white space

# To use any other character as a separator, define a sep parameter for the print() function.

city="Hyderabad"
state="Telangana"
country="India"
print(city, state, country, sep=',')

# ---------------------------------------------------------------------------------------------------------------------------------

# The print() function issues a newline character ('\n') at the end, by default. 
# As a result, the output of the next print() statement appears in the next line of the console.

# To make these two lines appear in the same line, define a end parameter 
# in the first print() function and set it to a whitespace string " ".

city="Hyderabad"
state="Telangana"
country="India"

print("City:", city, end=" ")
print("State:", state)

# ---------------------------------------------------------------------------------------------------------------------------------
