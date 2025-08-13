# creating  dict using curly braces
my_dict={"name": "John", "age": 30, "city": "New York"}
print(my_dict)
# print type dict
print(type(my_dict))


# creating dict with dict() constructor
# new_dict= dict(name="Alice", age=25, city="Los Angeles")
# print(new_dict)
 

 #functions of dict

print(len(my_dict))  # Length of the dictionary
print("name" in my_dict)  # Check if a key is in the dictionary
print(my_dict.get("age"))  # Get the value for a key
print(my_dict.keys())  # Get all keys in the dictionary
print(my_dict.values())  # Get all values in the dictionary
print(my_dict.items())  # Get all key-value pairs in the dictionary
my_dict["country"] = "USA"  # Add a new key-value pair
print(my_dict)
