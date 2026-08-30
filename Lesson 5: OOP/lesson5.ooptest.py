# return base raised to exponent (hint: ** is the power operator in Python)
#Test with power(3) (should be 9) and power(2, 3) (should be 8).

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))

# Test with Circle(5).area() — should print 78.5.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

print(Circle(5).area())

# loop through employees, call raise_salary(2000) on each,
# then print "Ana: 22000" / "Ben: 27000" using an f-string

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, amount):
        self.salary += amount

employees = [
    Employee("Ana", 20000),
    Employee("Ben", 25000),
]

for e in employees:
    e.raise_salary(2000)
    print(f"{e.name}: {e.salary}")
