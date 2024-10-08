#-----------------------------------------------------------------------------#
#               Link to this code is in the video description                 #
#-----------------------------------------------------------------------------#

# Primitive data type----------------------------------------------------------
x = 1                   # Integer
x = 1.2                 # Float
x = 1.0 + 2j            # Complex
x = "word"              # String
x = True                # Boolean
x = None                # None

# Conversion between primitive data types
int(2.1)                # float to integer
float(1)                # integer to float
bool(1)                 # integer to boolean 
str(1)                  # integer to string

# Derived data types ----------------------------------------------------------
my_list  = ["a", 2, "b"]           # list
my_tuple = ("a", 2, "b")           # tuple
my_range = range(3)                # range
my_set = {"a", 2, "b"}             # set
my_fset = frozenset({"a", 2, "b"}) # frozen set
my_dict = {"list": ["a", 2, "b"],  # dict
           "tuple": ["a", 2, "b"]}

# Conversion between derived data types
tuple(my_list)      # list to tuple
list(my_tuple)      # tuple to list
set(my_list)        # list to set 
set(my_dict)        # dict to set (only get keys)

# Access item of list, tuple, range
my_list[0]
my_tuple[0]
list(my_range)[0]


list(my_set)[0]
for item in my_set:
    print(item)

# Methods with list, tuple, set, frozenset, dict
my_list.append(34)   # append 34 to my list
my_list.pop(3)       # remove item with specific index from a list
my_list.clear()      # clear all items


