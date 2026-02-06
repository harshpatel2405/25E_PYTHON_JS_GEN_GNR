# * Symbol : []
# * Lists are mutable (you can change the value of list)
print()

fruits = ["Apple", "Banana", "Kiwi"]
print("Original List :", fruits)

# * 1. Update an element
fruits[1] = "Orange"
print("1. After Updating Directly :", fruits)

# * 2. Add an element (append an element)
fruits.append("PineApple")
print("2. After Appending :", fruits)

# * 3. Remove an element
fruits.remove("Kiwi")
print("3. After Removing :", fruits)

# * 4. Copy a list into another  (will return and need to store somewhere)
veggies = fruits.copy()
print("4. After Copying (Veggies) :", veggies)

# * 5. Count How many times a value is repeated (will return and need to store somewhere)
count = fruits.count("Kiwi")
print("5. After Count :", count)
# print("5. After Count :", fruits.count("Kiwi"))

# * 6. Extend a list
b = ["Litchie", "Dragon Fruit"]
fruits.extend(b)
print("6. After Extending :", fruits)


# for fruit in fruits:
#     # print(fruit, end=", ")
#     print(fruit)

# * 7. pop (removes last element)
fruits.pop()
print("7. After Pop :", fruits)

# * 8. insert
fruits.insert(2, "Strawberry")
print("8. After Insert :", fruits)

# * 9. index
index = fruits.index("PineApple")
print("9. After Index :", index)

# * 10. reverse
fruits.reverse()
print("10. After Reverse :", fruits)

# * 11. sort
fruits.sort()
print("11. After Sort :", fruits)

# * 12. clear
fruits.clear()
print("12. After Clear :", fruits)

print()
