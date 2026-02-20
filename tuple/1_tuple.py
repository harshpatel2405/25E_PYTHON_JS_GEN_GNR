# t = [1, 3, 10, 3, 4]
# print(t)
# s = tuple(t)
# print(s)

# # * 1. count method -- count of particular element
# print(s.count(3))

# # * 2. index
# print(s.index(4))
# print(s.index(3, 2, 4))

# print(len(s))
# print(max(s))
# print(min(s))
# print(sum(s))
# print(sorted(s))


# print(s[0])
# print(s[1:3])

# s1 = (1, 2)
# s2 = (3, 4)
# print(s1 + s2)

# print(s1 * 3)


# data = ("Harsh", 56, 12)

# for i in data:
#     print(i)

# name, marks, std = data
# print("Name :", name)
# print("marks :", marks)
# print("Std :", std)


# n = (1, 2, 3, 4, 5, 6)
# sum = 0
# for i in n:
#     print(i)
#     sum += i

# print("Sum :", sum)


# # * find min and max without using min() and max()
# smallest = n[0]
# largest = n[0]
# for i in n:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i

# print("Largest :", largest)
# print("Smallest :", smallest)


# tup = (10, 20, 30, 40, 50)

# print(tup)
# li = list(tup)

# li.append(60)

# tup = tuple(li)
# print(tup)


tuple = (10, 11, 12, 13, 14)
even = []
odd = []

for i in tuple:
    if i % 2 == 0:
        even.append(i)
        print("Even Inside :", even)
    else:
        odd.append(i)
        print("Odd Inside :", odd)

print("Even Outside :", even)
print("Odd Outside :", odd)
# tuple = (10, 11, 12, 13, 14)
# even = ()
# odd = ()

# for i in tuple:
#     if i % 2 == 0:
#         even = even +  (i,)
#         print("Even Inside :",even)
#     else:
#         odd += (i,)
#         print("Odd Inside :",odd)

# print("Even Outside :",even)
# print("Odd Outside :",odd)
