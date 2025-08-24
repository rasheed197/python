# Python match-case statement takes an expression and compares its 
# value to successive patterns given as one or more case blocks.

# Only the first pattern that matches gets executed.

# --------------------------------------------------------------------------------------------------------------------------------

# "_" serves as the wildcard case, and will be executed if all other cases are not true.

def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))

# --------------------------------------------------------------------------------------------------------------------------------

# Combined Cases in Match Statement 
# ---------------------------------

# You can combine cases with the OR operator represented by "|" symbol.

def access(user):
   match user:
      case "admin" | "manager": return "Full access"
      case "Guest": return "Limited access"
      case _: return "No access"
print (access("manager"))
print (access("Guest"))
print (access("Ravi"))

# --------------------------------------------------------------------------------------------------------------------------------

# List as the Argument in Match Case Statement
# --------------------------------------------

# You can also use a list as a case value. 
# Moreover, for variable number of items in the list, 
# they can be parsed to a sequence with "*" operator.

def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg

print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))

# --------------------------------------------------------------------------------------------------------------------------------

# Using "if" in "Case" Clause
# ---------------------------

def intr(details):
   match details:
      case [amt, duration] if amt<10000:
         return amt*10*duration/100
      case [amt, duration] if amt>=10000:
         return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))

# --------------------------------------------------------------------------------------------------------------------------------

