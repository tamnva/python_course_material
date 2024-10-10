#-----------------------------------------------------------------------------#
#             Link to this code is in the video description                   #       
#-----------------------------------------------------------------------------#

# 1. Conditional statement-----------------------------------------------------
x = 5

if x == 0:
    print("x is zero")
elif x > 0:
    print("x is postive")
else:
    print("x is negative")

# 2. Loop in python - For loop ------------------------------------------------
for i in range(5):
    print(i)

my_list = ["a", 2, "b", "c"]
my_set = {"aa", "bb", "cc"}
my_tuple = ("first", "second")
my_dict = {"key_one": my_list, "key_two": my_set}
second_list = [1, 2, 3, 4]

# Loop over the element
for element in my_list:
    print(element)

# Loop using index
for i in range(len(my_list)):
    print((i, my_list[i]))

# Loop using both index and element
for i, element in enumerate(my_list):
    print((i, element))

# Loop over two list together
for element_one, element_two in zip(my_list, second_list):
    print((element_one, element_two))

# Loop over the dict
for element in my_dict:
    print(element)
    print(my_dict[element])

# 3. Loop in python - While loop ----------------------------------------------

# While loop
i = 0
while i < 4:
    print(i)
    i += 1

# While loop over a list
i = 0
while i < 2:
    print((i, my_list[i]))
    i += 1

# 4. Break and continue in loop -----------------------------------------------

# Break only break the most inner-most loop
for i in range(5):
    for j in range(6):
        if j == 3:
            break
        print((i, j))

for i in range(10):
    if i == 3:
        continue
    print(i)
    print(i + 1)

# Note: if and loop cannot be empty, just use pass to do nothing
if i == 3:
    pass

for i in range(4):
    pass



























