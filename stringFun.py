# Example string
s = "  Hello, World!  "

# Length of the string
print("Length:", len(s))

# Convert to lowercase
print("Lowercase:", s.lower())

# Convert to uppercase
print("Uppercase:", s.upper())

# Remove leading and trailing whitespace
print("Stripped:", s.strip())

# Replace substring
print("Replace 'World' with 'Python':", s.replace("World", "Python"))

# Find substring
print("Index of 'World':", s.find("World"))

# Split string
print("Split by comma:", s.split(","))

# Join list into string
words = ["Hello", "Python"]
print("Join with space:", " ".join(words))

# Check start and end
print("Starts with '  He':", s.startswith("  He"))
print("Ends with 'World!  ':", s.endswith("World!  "))