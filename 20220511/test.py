
from re import L


class Student:
    def __init__(self, str):
        self.name = str
    
    def printStudent(self):
        print(self.name)
        
std = Student(input("학생이름= "))
std.printStudent()