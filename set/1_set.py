#
# * Set is an ordered Collection and does not allow duplicates
# * mutable
# * 1,2,3,2  -> 1, 2, 3

s = {1, 2, 3, 5, 4, 3, 45, 4}
print(s)

# * 1. add
s.add(5)
print("1. After Adding :", s)

# * 2. pop
s.pop()
print("2. After Popping :", s)

# * 3. remove
s.remove(4)
print("2. After Removing :", s)

# * 4. union
a = {1, 2, 3}
b = {4, 5, 6}

print("4. After Union :", a | b)
# print("4. After Union :",a.union(b))

# * 5. intersect
# print("5. After Intersection :", a & b)
print("5. After Intersection :", a.intersection(b))

# * 6. Subtract
print("6. After Subtract :", a.difference(b))

# * 7. Symmetric Difference
print("7. After Symmetric Difference :", a.symmetric_difference(b))

# * 8. Issubset
print("8. After Subset :", a.issubset(b))

# * 9. Issuperset
print("8. After Super Set :", a.issuperset(b))

# * 10. isDisjoint
print("10. After isDisjoint :", a.isdisjoint(b))

# * 11. clear
s.clear()
print("11. After Clear :", s)


'''

1.  Add & Remove Elements
Create a set of 5 fruits.
Add one new fruit
Remove one fruit
Check if "apple" exists in the set

2. Find union
Find intersection
Find elements only in A

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

3. Given two sets from user input:
Check if one is subset of another
Check if one is proper subset
Check if sets are equal
'''