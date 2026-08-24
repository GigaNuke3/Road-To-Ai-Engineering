# Challenge 1 

price = "100"
total = int(price) + 50
print(total)


# Challenge 2

subjects = ["Math", "Science", "English"] #-List use [] Set uses {}

for subject in subjects:
    print(f"Subjects: {subject}")


# Challenge 3

wallet = {"cash": 500, "gcash": 300}
balance = wallet["cash"] + wallet["gcash"]
print(f"Total Balance: {balance}")

# Challenge 4

score = {"Charles": 90, "Eco": 95, "Miguel": 88}
for key, value in score.items():
    if value > 89:
        print(f"{key} passed with {value}")

   