# * 
# * Tuple is immutable 

t = (10, 20, 30, 40, 10, 10, 20)
print(t)

t1 = (20, 19, 18, 17)
print(t1)

# * 1. count -- will return how many times a particular element is repeated
print(t.count(10))

# * 2. index
print(t.index(20))

# * 3. length
print(len(t))

# * 4. Access element - by index
print(t[3])

# * 5. slice
print(t[1:5])
print(t[1:5:2])

# * 6. concate
t1 = (1, 2, 3, 45)
t2 = (9, 7, 8, 9, 10)
print(t1 + t2)

# * 6. Repetition
print(t1 * 3)

# * 7. check
print(45 in t1)

for i in t1:
    print(i, end=", ")
