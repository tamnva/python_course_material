#-----------------------------------------------------------------------------#
#           Link to this code is in the video description                     #
#-----------------------------------------------------------------------------#

# Read text file---------------------------------------------------------------
f = open(file="C:/examples/text_file.txt", mode="r")
f.read()
f.close()

# Read single line
f = open(file="C:/examples/text_file.txt", mode="r")
f.readline()
f.close()

# Read all lines
f = open(file="C:/examples/text_file.txt", mode="r")
f.readlines()
f.close()

# Good practice
with open(file="C:/examples/text_file.txt", mode="r") as f:
    content = f.read()


# Write text file--------------------------------------------------------------

# Write to a file
with open(file="C:/examples/my_file.txt", mode="a") as f:
    f.write(str(1235000))

