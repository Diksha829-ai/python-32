# Multilevel Inheritance Example
class Grandparent:
    def show_grandparent(self):
        print("I am the Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am the Parent")

class Child(Parent):
    def show_child(self):
        print("I am the Child")


# Create object of Child
c = Child()

# Child has access to all methods
c.show_grandparent()
c.show_parent()
c.show_child()
