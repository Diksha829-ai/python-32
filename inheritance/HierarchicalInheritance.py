# Hierarchical Inheritance Example
class Parent:
    def feature1(self):
        print("Common Feature from Parent")

class Child1(Parent):
    def feature2(self):
        print("Feature from Child1")

class Child2(Parent):
    def feature3(self):
        print("Feature from Child2")

c1 = Child1()
c1.feature1()
c1.feature2()

c2 = Child2()
c2.feature1()
c2.feature3()
