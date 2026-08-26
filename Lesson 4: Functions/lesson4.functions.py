
# Challenge 1 - return "Pass" if score >= 60, else return "Fail"

def check_grade(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

print(check_grade(75))
print(check_grade(40))

# Challenge 2 - loop through the list and print each item
# Test with print_all(["Math", "Science", "English"]).

def print_all(items):
    
    for item in items:
        print(item)

print_all(["Math", "Science", "English"])

#Challenge 3 - Function returning from a dict
# grades is a dict like {"Charles": 90, "Eco": 95}
# return the grade for the given student name
# Test with get_grade("Eco", {"Charles": 90, "Eco": 95}) — should return 95

def get_grade(student, grades):

    return grades[student]

result = get_grade("Eco", {"Charles": 90, "Eco": 95})
print(result)



#Challenge 4 - Function + set, real-world flavor
#items is a list, possibly with duplicates
#return the count of unique items (not items themselves - a number)
#Test with unique_count(["a", "b", "a", "c", "b"]) — should return 3


def unique_count(items):
    return len(set(items))

result = unique_count(["a", "b", "a", "c", "b"])
print(result)