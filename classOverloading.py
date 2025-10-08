# class overloading
class Student:
    def __init__(self, name, age=None, grade=None):
        self.name = name
        self.age = age
        self.grade = grade


    def display(self):
        info = f"Name: {self.name}"
        if self.age is not None:
            info += f", Age: {self.age}"
        if self.grade is not None:
            info += f", Grade: {self.grade}"
        print(info)

        
# Creating instances with different parameters
s1 = Student("Alice")
s2 = Student("Bob", 20)
s3 = Student("Charlie", 22, "A")
s1.display()  # Output: Name: Alice
s2.display()  # Output: Name: Bob, Age: 20
s3.display()  # Output: Name: Charlie, Age: 22, Grade: A
