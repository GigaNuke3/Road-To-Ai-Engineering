
def unique_count(items):
    unique = set(items)
    return len(unique)

print(unique_count(["a", "b", "a", "c", "b"]))
print(unique_count([1, 1, 1, 2, 2, 3]))
print(unique_count(["x", "y", "z"]))
print(unique_count([5, 5, 5, 5]))   # should be 1 — only one unique valueoto