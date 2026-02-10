#  Magic methods = Dunder methods (double underscore) __init__, __self__, __eq__
#                  They are automatically called by many of Python's built-in operations
#                  They allow developers to define or customuze the behavior of objects

class Student:
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        
    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
    def __lt__(self, other):
        return self.gpa < other.gpa
    
    def __add__(self, other):
        return self.gpa + other.gpa
    
    def __contains__(self, keyword):
        return keyword in self.name
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
    
student1 = Student("Spongebob Square pants", 3.2)
student2 = Student("Patric", 2.0)
student3 = Student("Sandy", 4.0)

print(student1)
print(student1 == student2)
print(student1 > student2)
print(student1 < student2)
print(student1 + student2)
print("pants" in student1)
print(student1["name"])