# print "Hot" if temperature >= 35
# print "Warm" if temperature >= 25
# print "Cold" if below 25

temperature = 33

if temperature >= 35:
    print("Hot")
elif temperature >= 25:
    print("Warm")
else:
    print("Cold")

# Fix the unreachable branch

#-----------------
#speed = 80

#if speed > 60:
#    print("Fast")
#elif speed > 80:
#    print("Very fast")
#$else:
#    print("Normal")
#-----------------

speed = 80

if speed > 80:
    print("Very fast")
elif speed > 60:
    print("Fast")
else:
    print("Normal")

# 1. get only the unique visitor names using a set, print it
# 2. print how many unique visitors there are (hint: len() works on sets too)

visitors = ["Ana", "Ben", "Ana", "Cara", "Ben", "Ana"]
unique_visitor = set(visitors)
print(len(unique_visitor))


# loop through inventory
# for each item, print "apples: in stock" if quantity > 0
# print "bananas: out of stock" if quantity == 0

inventory = {"apples": 12, "bananas": 0, "mangoes": 5}

for key, value in inventory.items():
    if value > 0:
        print(f"{key}: in stock")
    else:
        print(f"{key}: out of stock")

