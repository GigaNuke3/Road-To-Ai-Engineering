
def safe_divide(a, b):
    try: 
        return a/b
    except ZeroDivisionError:
        return "Cannot Divide by zero"
    except TypeError:
        return "Invalid input"
    finally:
        print("Divide attempt finished")

print(safe_divide(10, 2))
print(safe_divide(10,0))
print(safe_divide(10, "a"))