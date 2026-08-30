
def divide (a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return"Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0)) 

    
