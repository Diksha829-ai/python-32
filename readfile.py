f=open("Sample.txt","r")
# Read the entire content of the file
content=f.read()
# Print the content
print(" Read the File Content:\n", content)


# seek function is used to change the file cursor position
f.seek(3)   # move cursor to the 5th byte
content = f.read()


# read function is used to read the content of the file
print("Content after seeking to 5th byte:\n", content)


# Reset cursor to the beginning before readline
f.seek(0)
# readline function is used to read a single line from the file
f.readline()  # Read the first line
readline = f.readline()  # Read the next line
print("Content after reading a line:\n", readline)


# Reset cursor again before readlines
f.seek(0)
# readlines function is used to read all lines from the file
readlines = f.readlines()  # Read all lines into a list
print("All lines in the file:\n", readlines)

# close the file
f.close()
