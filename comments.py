# Comments in Python are non-executable lines used to explain code, add notes, 
# or temporarily disable code sections.

# The Python interpreter ignores comments during program execution.

# ------------------------------------------------------------------------------------------------------------------

# Python supports two types of comments
# 1. Single-line Comments
# 2. Multi-line Comments

# ------------------------------------------------------------------------------------------------------------------

# Single-line Comments

# Single-line comments begin with a hash symbol (#).

# This is a single-line comment
print("Hello, World!") # This comment explains the print statement

# ------------------------------------------------------------------------------------------------------------------

# Multi-line Comments - This is divided into two
# 1. Multiple single-line comments
# 2. Multi-line strings (docstrings)

# ------------------------------------------------------------------------------------------------------------------

# Multiple single-line comments

# This is a multi-line comment
# created by using multiple
# single-line comments.
print("Multi-line comment example")

# ------------------------------------------------------------------------------------------------------------------

# Multi-line strings (docstrings) - using ''' or """

"""
This is also a form of multi-line comment,
often used as docstrings for functions or modules.
"""
print("Using a multi-line string as a comment")

# ------------------------------------------------------------------------------------------------------------------

# Using Comments for Documentation

# Python docstrings are a special type of comment that is used to 
# document modules, classes, functions, and methods.

# They are written using triple quotes (''' or """) and are placed 
# immediately after the definition of the entity they document.

# ------------------------------------------------------------------------------------------------------------------

# Example of a Function Docstring for Documentation

def greet(name):
   """
   This function greets the person whose name is passed as a parameter.

   Parameters:
   name (str): The name of the person to greet

   Returns:
   None
   """
   print(f"Hello, {name}!")
greet("Alice")

# ------------------------------------------------------------------------------------------------------------------

# Accessing Docstrings
# Docstrings can be accessed using the .__doc__ attribute or the help() function.

print(greet.__doc__) # OR
help(greet)

# ------------------------------------------------------------------------------------------------------------------
