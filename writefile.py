
# Open the file in write mode
f=open("Sample.txt","w")

# write the content in the file
f.write("This is a sample file.\n")
f.write("It contains multiple lines.\n")
f.write("This is the third line.\n")
f.write("I am Diksha, a student of TY CSE.\n")
f.write("I am learning Python.\n")
f.write("This is the last line.\n")


# close the file
f.close()

# Open the file in read mode
f = open("Sample.txt", "r")
# Read the entire content of the file
content = f.read()
# Print the content
print("write the File Content:\n", content)
# Close the file
f.close()
