fruits={"banana", "apple", "cherry", "mango", "orange"}
# Display the set
print("Fruits Set:", fruits)

#function on set
# Adding an element
fruits.add("kiwi")
print("Fruits Set after adding kiwi:", fruits)

# Removing an element
fruits.remove("banana")
print("Fruits Set after removing banana:", fruits)

# Discarding an element
fruits.discard("apple")
print("Fruits Set after discarding apple:", fruits)

# Popping an element
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("Fruits Set after popping an element:", fruits)

# Checking membership
print("Is 'cherry' in fruits?", "cherry" in fruits)

# Length of the set
print("Length of fruits set:", len(fruits))

