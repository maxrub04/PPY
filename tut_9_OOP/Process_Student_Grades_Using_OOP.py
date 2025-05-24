"""
Write a Python program that processes student grade data using Object-Oriented
Programming (OOP). Your program will:
• Read data from a text file
• Create objects for each student
• Compute total grades
• Determine pass/fail status
• Write results to a new output file, automatically created in the same folder as the
script
This task reinforces:
• Reading and writing text files
• Designing and using Python classes
• Basic error handling with files
"""
import pathlib

class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def total_score(self):
        return sum(self.grades)

    def has_passed(self):
        if self.total_score()>=180:
            return True
        else:
            return False

class StudentManager:
    STATUS_PASSED = "PASSED"
    STATUS_FAILED = "FAILED"
    DELIMITER = ","

    def __init__(self, file_path):
        self.file_path = pathlib.Path(file_path)
        self.students = []

    def read_students(self):
        try:
            with self.file_path.open('r') as file:
                for line in file:
                    names_and_grades = line.strip().split(self.DELIMITER)
                    name = names_and_grades[0].strip()
                    grades = list(map(int, names_and_grades[1:]))
                    student = Student(name, grades)
                    self.students.append(student)
        except FileNotFoundError:
            print("File not found. Please provide a valid file path.")

    def write_results(self, output_path):
        output_path = pathlib.Path(output_path)
        with output_path.open('w') as f:
            for student in self.students:
                status = self.STATUS_PASSED if student.has_passed() else self.STATUS_FAILED
                f.write(f"{student.name}: Total = {student.total_score()}, Status = {status}\n")


input_path = "grades_input.txt"
output_path = "grades_output.txt"

manager = StudentManager(input_path)
manager.read_students()

manager.write_results(output_path)