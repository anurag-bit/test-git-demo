class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_info(self):
        print("Student Information:")
        print("Name:", self.name)
       


name = input("Enter student name: ")    
age = input("Enter student age: ")
grade = input("Enter student grade: ")

student = Student(name, age, grade)

student.print_info()
