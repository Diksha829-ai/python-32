# copy the content of sample.txt to copy.txt
with open("Sample.txt", "r") as f1, open("Copy.txt", "w") as f2:
    content = f1.read()
    f2.write(content)

print(content) # Print the copied content

print("File content copied successfully!")

