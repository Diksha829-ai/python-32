import array as arr

# i for integer
# Create an array of integers
int_array = arr.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)

# Create an array of floats
# 'f' for float
float_array = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print("Float Array:", float_array)

# Instead of using 'u' (deprecated), use a list of characters
char_array = list("hello")
print("Character Array:", char_array)
