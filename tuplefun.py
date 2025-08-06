my_tuple = (10, 20, 30, 20, 40, 50)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Length of tuple
print("Length:", len(my_tuple))

# Slicing
print("Slice [1:4]:", my_tuple[1:4])

# Check existence
print("Is 20 in tuple?", 20 in my_tuple)

# Count occurrences
print("Count of 20:", my_tuple.count(20))

# Index of element
print("Index of 30:", my_tuple.index(30))

# Concatenation
another_tuple = (60, 70)
concatenated = my_tuple + another_tuple
print("Concatenated tuple:", concatenated)

# Repetition
repeated = my_tuple * 2
print("Repeated tuple:", repeated)

# Convert to list and back
my_list = list(my_tuple)
print("Converted to list:", my_list)
new_tuple = tuple(my_list)
print("Converted back to tuple:", new_tuple)
