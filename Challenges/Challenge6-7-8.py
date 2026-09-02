
import requests

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def status(self):
        if self.grade >= 60:
            return "Passed"
        else:
            return "Failed"

students = [
    Student("Charles", 90),
    Student("Eco", 55),
    Student("Miguel", 90),
]

for s in students:
    print(f"{s.name}: {s.grade}")

# return "Passed" if grade >= 60, else "Failed"

def save_students_to_file(students, filename):
    with open(filename, "w") as file:
        for student in students:
            file.write(f"{student.name},{student.grade}\n")
        
save_students_to_file(students, "records.txt")

# loop through students, write each one to the file as:
# "Charles,90\n" (name, comma, grade, newline)
# use "w" mode


def load_students_from_file(filename):
    try:
        with open(filename, "r") as file:
            students = []
            for line in file:
                line = line.strip()
                if line:
                    name, grade = line.split(",")
                    students.append(Student(name, int(grade)))
        return students
    except FileNotFoundError:
        return []

loaded = load_students_from_file("records.txt")
for s in loaded:
    print(f"{s.name}: {s.status()}")

# try to open and read the file
# if it doesn't exist, catch FileNotFoundError and return an empty list
# otherwise, split each line by comma, create Student objects, return them as a list
# (hint: file.read().splitlines() gives you a list of lines without \n)

def unique_grades(students):
    grades = []
    for student in students:
        grades.append(student.grade)
    return len(set(grades))
print("Unique grades:", unique_grades(loaded))

# given a list of Student objects, return the count of unique grade values
# (hint: pull out grade values into a list first, then use a set)