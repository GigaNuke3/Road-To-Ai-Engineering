
# 1. convert scores into a set to get only unique values, print it
# 2. add 95 to the set
# 3. try scores[0] — see what error you get, then remove that line

scores = [85, 90, 85, 78, 90, 100, 78]
unique_numbers = set(scores)
print(unique_numbers)

unique_numbers.add(95)
print(unique_numbers)

print(scores[0])


try:
    print(unique_numbers[0])
except TypeError as e:
    print("Error:", e)

# SET and LIST works relative to what enclosing braces are pointed to

scores = [85, 90, 85, 78]
unique_numbers = set(scores)

print(scores)           # still the original list, duplicates and all
print(unique_numbers)    # the new set, duplicates removed