
# * map -- returns all elements present (might update them)
# ^ map(function , iterable)
from functools import reduce
num = [10, 11, 12, 13, 14]
square = map(lambda x: x*x, num)
print(list(square))

even = map(lambda x: x % 2 == 0, num)
print(list(even))


# * filter -- returns only those who satisfies the condition
num = [10, 11, 12, 13, 14]
square = filter(lambda x: x > 11, num)
print(list(square))

even = filter(lambda x: x % 2 == 0, num)
print(list(even))

# * reduce -- reduce it to single value  (acc, curr)
res = reduce(lambda x, y: x+y, num)
print(res)

# * zip
name = ["Harsh", "Vedant", "Dev"]
marks = [99, 88, 77]

print(list(zip(name , marks)))
