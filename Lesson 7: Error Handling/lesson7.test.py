def read_student_file(filename):
    try:
        with open("students.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found"
    finally:
        print("Read attempt finished")

print(read_student_file("students.txt"))

with open("students.txt", "w") as file:
    file.write("Charles, Eco, Miguel")

print(read_student_file("students.txt"))