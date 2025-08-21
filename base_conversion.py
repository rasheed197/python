# Convert from base 10 to base 2
x=60 # base 10
x_b2=bin(x) # base 2

print("60 to base2 - ", x_b2) # 0b111100

# ----------------------------------------------------------------------------------------------------------------------

# convert from base 2 to base 10
x_b2="00111100" # Make sure its 8-bit
x=int(x_b2, 2) # convert base 2 to base 10

print("00111100 to base 10 - ", x) # 60