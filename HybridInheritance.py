#hybrid Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):   # Single
    def showB(self):
        print("Class B")

class C(A):   # Hierarchical
    def showC(self):
        print("Class C")

class D(B, C):   # Multiple
    def showD(self):
        print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()
