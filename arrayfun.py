import array as arr

# i for integer
# Create an array of integers
int_array = arr.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)

# function on array
# 1 append function
int_array.append(6)
print("After appending 6:", int_array)

# 2 insert function

int_array.insert(0, 0)  # Insert 0 at the beginning
print("After inserting 0 at the beginning:", int_array)

# 3 extend function
int_array.extend([7, 8, 9])  # Extend with multiple values
print("After extending with [7, 8, 9]:", int_array)

# 4 remove function
int_array.remove(5)  # Remove the first occurrence of 5
print("After removing 5:", int_array)

# 5 pop function
popped_value = int_array.pop()  # Pop the last value
print("Popped value:", popped_value)
print("After popping the last value:", int_array)

# 6 index function
index_of_3 = int_array.index(3)  # Find the index of the first occurrence of 3
print("Index of 3:", index_of_3)    

# 7 count function
count_of_2 = int_array.count(2)  # Count occurrences of 2
print("Count of 2:", count_of_2)

# 8 reverse function
int_array.reverse()  # Reverse the array
print("After reversing the array:", int_array)



