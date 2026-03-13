#  *
#  * set {} ordered
# * it removes duplicates

# * 1. Normal Printing
s = {1, 2, 3, 4}
print("1. Normal Printing :", s)

# s1 = {4, 3, 2, 1}
# print(s)

# s2 = {1, 2, 3, 4, 5, 6, 6, 4, 3, 2, 1, 1, 20}
# print(s2)

# * 2. add data
s.add(11)
print("2. add data :", s)


# s2.add(11)
# print(s2)
# print(s2)

# * 3. pop data
s.pop()
print("3. pop data :", s)

# s2.pop()
# print(s2)

# * 4. remove data
s.remove(11)
print("4. remove data(11) :", s)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
# * 5. union
print("5. union  (s1 union s2) :", s1 | s2)

# * 6. Intersection
print("6. Intersection (s1 & s2) :", s1 & s2)

# * 7. Difference
print("7. Difference (s1-s2) :", s1 - s2)

# * 8. Symmetric Difference
print("8. Symmetric Difference s1 ^ s2 :", s1 ^ s2)

print("s1.issubset(s2) :", s1.issubset(s2))
print("s1.issuperset(s2) :", s1.issuperset(s2))
print("s1.isdisjoint(s2) :", s1.isdisjoint(s2))

# * 9. Clear
s.clear()
print("9. Clear :", s)

'''
#* Task : day1 = {"Rahul", "Amit", "Neha"}
#*        day2 = {"Neha", "Amit", "Sita"}

# & 1. Unique Visitors on day 2 
# & 2. Total Unique visitors in both days 

#* 2. Task : submitted = {"A", "B", "C", "D"}
#*           all_students = {"A", "B", "C", "D", "E", "F"}
# &  1. How many students did not submit ?
#
#
'''