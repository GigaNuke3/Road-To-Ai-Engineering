

book = {"title": "Atomic Habits", "author": "James Clear", "pages": 320}

# 1. print the author
# 2. update pages to 350
# 3. add a new key "genre" with value "Self-help"
# 4. loop through the whole dict us
#    "title:ing .items() and print each as: Atomic Habits" etc.

print(book["author"])
book["pages"] = 350
book["genre"] = "Self-help"

for key, value in book.items():
    print(f"{key}: {value}")
