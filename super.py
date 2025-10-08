# use of super in python

class Parent:
    def show(self):
        print("Parent class method called")
class Child(Parent):
    def show(self):
        super().show()  # Call method from Parent class
        print("Child class method called")
        
# Create instance of Child
c = Child()
c.show()