
# Lists - ordered collection, like PHp's indexed array

fruits = ["apple", "banana", "mango"]

print(fruits[0])
fruits.append("grape")
fruits.append("olive")
print(len(fruits))
print(fruits)

## Notes — Lesson 2, Part 1: Lists
#
#**What a list is**
#- Ordered collection of items, like PHP's indexed array
#- Square brackets: `fruits = ["apple", "banana", "mango"]`
#- Zero-based indexing — first item is `[0]`, not `[1]`
#```python
#fruits[0]   # "apple"
#fruits[1]   # "banana"
#fruits[2]   # "mango"
#```
#Indexing picks **one item by position** — it doesn't loop or wrap around.
#
#**`.append()`**
#- Adds an item to the **end** of the list
#- Equivalent to PHP's `array_push()`
#- Each `.append()` call grows the list by exactly one item
#```python
#fruits.append("grape")   # list is now 4 items
#fruits.append("olive")   # list is now 5 items
#```
#
#**`len()`**
#- Built-in function that returns "how many items right now"
#- Not list-specific — works on strings, lists, dicts, etc.
#```python
#len("hello")          # 5 (characters)
#len([1, 2, 3])         # 3 (list items)
#len({"a": 1, "b": 2})  # 2 (key-value pairs)
#```
#- Python's one `len()` replaces PHP's separate `strlen()` / `count()`
#
#**Order of execution matters**
#- Python runs top to bottom, one line at a time
#- `len()` (or any print) reports the state of the list **at that exact line** — not the final state
#```python
#fruits.append("grape")
#print(len(fruits))   # includes grape
#fruits.append("olive")
#print(len(fruits))   # includes grape AND olive
#```
#- Where you place a check like `len()` changes *what moment* it's reporting on — useful for tracking state as things get added, not just a final total
#
#---
#
#