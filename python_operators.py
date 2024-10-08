#-----------------------------------------------------------------------------#
#               Link to this code is in the video description                 #
#-----------------------------------------------------------------------------#

# 1. Arithmetic----------------------------------------------------------------
x = 5.0; y = 2.0
x + y            # Addition
x - y            # Subtraction
x * y            # Multiplication
x % y            # Modulus (remainder of the division)
x ** y           # Exponent
x / y            # Division
x // y           # Floor division (round down to the nearest integer)

# 2. Assignment----------------------------------------------------------------
x = 5.0    # Assign 5 to x
x += 2.0   # x = x + 2
x -= 2.0   # x = x - 2
x *= 2.0   # x = x * 2
x /= 2.0   # x = x / 2
x %= 2.0   # x = x % 2.0
x //= 2.0  # x = x // 2.0


# 3. Comparision---------------------------------------------------------------
x = 5.0; y = 2.0
x > y           # Greater than
x < y           # Smaller thant
x == y          # Equal to
x <= y          # Smaller or equal to
x >= y          # Greater or equal to 

# 4. Logical-------------------------------------------------------------------
x > 0 and y > 0        # Only True if both are True
x > 0 or y > 0         # Only False if both are False
not(x > 0)             # True if result is False and vice versa

# 5. Identity------------------------------------------------------------------
# Compare the objects to determine whether they share the same memory location
#                                               and refer to the same data type
# There are two identity operator 'is' and 'is not'

x = 5.0; y = 5.0; z = x
x is y    
z is x
id(x)         # Get memory location of x
id(y)         # Get memory location of x
id(z)         # Get memory location of x
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a is c
a is b

# 6. Membership----------------------------------------------------------------

5 in [1, 2, 5]          # check if 5 in a list
5 not in [1, 2, 5]      # check if 5 is not in a list

'a' in {'a', 2, 'b'}    # check if a in a set
'c' in ('a', 'c', 2)    # check if c in a tuple
'key_3' in {'key_1': 1, 'key_2': 'a'}  # check if key_1 in a dict keys

# 7. Bitwise-------------------------------------------------------------------
0 & 0
1 & 1
# For more please visit https://wiki.python.org/moin/BitwiseOperators

