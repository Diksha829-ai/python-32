#access specifire in python

class Student:
    def __init__(self, name, age, roll):
        self.name = name # Public attribute
        self._age = age # Protected attribute
        self.__roll = roll  # Private attribute

    # Public method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age (Protected): {self._age}")
        print(f"Roll (Private): {self.__roll}")

    # Getter for private variable
    def get_roll(self):
        return self.__roll


# Object creation
s = Student("Diksha", 20, 101)

# Public - directly accessible
print(s.name)  

# Protected - can be accessed (not recommended)
print(s._age)  

# Private - cannot be accessed directly
# print(s.__roll)   # ❌ AttributeError

# Access private via method
print(s.get_roll())  
