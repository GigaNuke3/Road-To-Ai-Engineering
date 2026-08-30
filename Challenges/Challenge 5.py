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
    Student("Miguel", 60),
]

for s in students:
    print(f"{s.name}: {s.status()}")