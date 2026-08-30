
with open("log.txt", "w") as file:
    file.write("Learning Python")

with open("log.txt", "r") as file:
    content = file.read()
    print(content)

#--------------------------


with open("log.txt", "a") as file:
    file.write("\nDay 2 complete")

with open("log.txt", "r") as file:
    content = file.read()
    print(content)


