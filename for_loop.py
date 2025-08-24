# The for loop provides the ability to loop over a sequence (such as a list, tuple, string, etc) 
# or other iterable objects (dictionary, set, etc). 

# It allows a block of code to be executed for each item in the sequence.

# ---------------------------------------------------------------------------------------------------------------------------

# Python for Loop with Strings
# ----------------------------

# The following example compares each character and displays if it is not a vowel ('a', 'e', 'i', 'o', 'u').
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char, end='')
      
# ---------------------------------------------------------------------------------------------------------------------------
      
# Python for Loop with Tuples
# ---------------------------

numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
   total += num
print ("Total =", total)

# ---------------------------------------------------------------------------------------------------------------------------

# Python for Loop with Lists
# --------------------------

numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)
      
# ---------------------------------------------------------------------------------------------------------------------------
      
# Python for Loop with Range Objects
# ----------------------------------

# range() function returns an iterator object that streams a sequence of numbers.
# This object contains integers from start to stop, separated by step parameter.

# The range() function has the following syntax −
# range(start, stop, step)

# Start − Starting value of the range. Optional. Default is 0
# Stop − The range goes upto stop-1
# Step − Integers in the range increment by the step value. Optional, default is 1.

for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')
   
# ---------------------------------------------------------------------------------------------------------------------------

# Python for Loop with Dictionaries
# ---------------------------------

# dictionary data type in Python is not a sequence, as the items do not have a positional index.
# However, looping through a dictionary is still possible with the for loop.

# Running a for loop on a dictionary returns the dictionary key
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x)

# Once we are able to get the key, its associated value can be easily accessed either 
# by using square brackets operator [] or with the get() method.
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])
   
# The items(), keys() and values() methods of dict class return 
# the view objects dict_items, dict_keys and dict_values respectively.

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# .items()
for x in numbers.items():
   print(x)
# OUTPUT -
# (10, 'Ten')
# (20, 'Twenty')
# (30, 'Thirty')
# (40, 'Forty')

# .keys()
for x in numbers.keys():
   print (x)
# OUTPUT -
# 10
# 20
# 30
# 40

# .values()
for x in numbers.values():
   print (x)
# OUTPUT - 
# Ten
# Twenty
# Thirty
# Forty

# ---------------------------------------------------------------------------------------------------------------------------

# Using else Statement with For Loop
# ----------------------------------

#For loop to iterate between 10 to 20
for num in range(10, 20):  
   #For loop to iterate on the factors 
   for i in range(2,num): 
      #If statement to determine the first factor
      if num%i == 0:      
         #To calculate the second factor
         j=num/i          
         print (f"{num} equals {i} * {j}") 
         #To move to the next number
         break 
      else:                  
         print (num, "is a prime number")
         break

# ---------------------------------------------------------------------------------------------------------------------------

