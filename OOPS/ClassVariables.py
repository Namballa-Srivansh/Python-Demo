# class variables = shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

# instance variables are declared inside the constructor

class Student:
    
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Vansh", 20)
student2 = Student("Dev", 21)
student3 = Student("Spongebob", 30)

# print(f"{student1.name} {student1.age} {Student.class_year}")
# print(f"{student2.name} {student2.age} {Student.class_year}")
# print(f"{student3.name} {student3.age} {Student.class_year}")

# print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")