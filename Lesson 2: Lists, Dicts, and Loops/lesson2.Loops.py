

students = ["Charles", "Eco", "Miguel"]

for student in students:
    print(student)

for student in students:
    print(f"Student: {student}")


#always remember plural and singular

grades = {"Charles": 90, "Eco": 95, "Miguel": 88}

for key, value in grades.items():
    print(f"{key} scored {value}")


print("--------------------")

grades = {"Charles": 90, "Eco": 95}

for name in grades:
    print(name)

print("---")

for name, score in grades.items():
    print(name, score)