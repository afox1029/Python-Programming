# Program that puts data on students into  a table
# 4/4/2023
# CSC221 M4HW – Students Class
# Alexander Jones
#
# Make a place to store student data
# Create three Student objects
# Display data for each student as a table

class Student:
    def __init__(self, id_number, first_name, last_name, major):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def __str__(self):
        return f"{self.id_number:5} {self.first_name:18} {self.last_name:12} {self.major:10}"



student1 = Student(47899, "      Susan", "Meyers", "Accounting")
student2 = Student(39119, "      Mark", "Jones", "Programmer")
student3 = Student(81774, "      Joy", "Rogers", "Engineering")


table_headers = "ID Number   First Name   Last Name    Major"
print(table_headers)
print("-" * len(table_headers))

print(student1)
print(student2)
print(student3)
print("-" * len(table_headers))
