# The if-else statement in Python is used to execute a block of code when the condition in the 
# if statement is true, and another block of code when the condition is false.

# Here, variable age can take different values. If the expression age > 18 is true, 
# then eligible to vote message will be displayed otherwise not 
# eligible to vote message will be displayed.

age=25
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")
   
# ------------------------------------------------------------------------------------------------------------------------
   
# Python if elif else Statement
# -----------------------------

# The if elif else statement allows you to check multiple expressions for TRUE 
# and execute a block of code as soon as one of the conditions evaluates to TRUE.

# The keyword elif is a short form of else if.

# Similar to the else block, the elif block is also optional.

# However, a program can contains only one else block whereas there can be 
# an arbitrary number of elif blocks following an if block.

# Example
amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)

# ------------------------------------------------------------------------------------------------------------------------

