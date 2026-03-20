from functools import reduce

a = lambda x: x * 5
print(a(5))


nums = [10, 20, 31, 40]

res = list(map(lambda x: x * x, nums))
print(res)

res = list(filter(lambda x: x % 2 == 0, res))
print(res)

res = reduce(lambda x, y: x + y, res)
print(res)
"""
nums = [12, -3, 7, 0, 25, -10, 8, 15]
-> Remove all negative numbers and zeros
-> For remaining numbers:
    -> If number is even → square it
    -> If number is odd → cube it
-> Keep only values that are divisible by both 3 and 5
-> Find the difference between the maximum and minimum using reduce()
"""

nums = [12, -3, 7, 0, 25, -10, 8, 15]

# * Remove all negative numbers and zeros
filter1 = list(filter(lambda x: x > 0, nums))

# * Even -> Square, odd -> cube
map1 = list(map(lambda x: x**2 if x % 2 == 0 else x**3, filter1))

# * Keep only values that are divisible by 3 and 5
filter2 = list(filter(lambda x: x % 15 == 0, map1))

# * max from list
max = reduce(lambda x, y: x if x > y else y, filter2)

# * min from list
min = reduce(lambda x, y: x if x < y else y, filter2)

print(filter2)
print("Difference : ",max-min)
