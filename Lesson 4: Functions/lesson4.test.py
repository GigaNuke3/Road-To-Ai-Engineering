
def get_price(item, prices):
    return prices[item]

print(get_price("banana", {"apple": 20, "banana": 10}))
print(get_price("apple", {"apple": 20, "banana": 10}))