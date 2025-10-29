# Multiple Inheritance Example
class Father:
    def skills(self):
        print("Father: Gardening, Cooking")

class Mother:
    def skills(self):
        print("Mother: Painting, Singing")

class Child(Father, Mother):   # Multiple inheritance
    def skills(self):
        # Call methods from both parents
        Father.skills(self)
        Mother.skills(self)
        print("Child: Coding, Dancing")


# Create object
c = Child()
c.skills()

