#hybrid Inheritance

# Base Class
class Student:
    def __init__(self, name):  # Base class constructor
        self.name = name

    def show_student(self):
        print("Student Name:", self.name)

# Derived from Student
class Exam(Student):
    def __init__(self, name, marks): # Derived class constructor
        Student.__init__(self, name)   # Direct call
        self.marks = marks

    def show_exam(self):
        print("Exam Marks:", self.marks)

# Derived from Student
class Project(Student): 
    def __init__(self, name, project_score):
        Student.__init__(self, name)   # Direct call
        self.project_score = project_score

    def show_project(self):
        print("Project Score:", self.project_score)

# Derived from Exam and Project (Hybrid Inheritance)
class Result(Exam, Project): 
    def __init__(self, name, marks, project_score):
        Exam.__init__(self, name, marks)        # Explicit calls
        Project.__init__(self, name, project_score)

    def show_result(self):
        total = self.marks + self.project_score
        print(f"Final Result for {self.name}: {total} marks")

# ----------------------------
# Execution
r = Result("Diksha", 90, 90)
r.show_student()
r.show_exam()
r.show_project() 
r.show_result()
