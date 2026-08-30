class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(f"{self.name} scored {self.grade}" )

student1 = Student("Charles", 90)
student2 = Student("Eco", 95)

student1.show()
student2.show()

student1.grade = 100
print(student1.grade)
print(student2.grade)

