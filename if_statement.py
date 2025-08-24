# The if statement in Python evaluates whether a condition is true or false.

# If the boolean expression evaluates to TRUE, then the statement(s) inside the if block is executed. 
# If boolean expression evaluates to FALSE, then the first set of code after the end of the if block is executed.

# The example below is of a customer entitled to 10% discount if 
# his purchase amount is > 1000; if not, then no discount is applicable.

discount = 0
amount = 1500

# Check he amount value
if amount > 1000:
   discount = amount * 10 / 100

print("amount = ", amount - discount)

