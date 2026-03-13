def add():
    a = 5
    b = 9
    print("sum of a and b is", a + b)


def subtract(a, b):
    print("subtraction of a and b is", a - b)


def multiply():
    a = 7
    b = 9
    return a * b


def divide(a, b):
    return a // b


add()
subtract(12, 5)
print("multiplication of a and b is", multiply())

print("Division of a and b is", divide(10, 6))


def greet(name="User"):
    print("Welcome", name)


greet("Harsh")


# recursion - function calling itself (back condition)
def countDown(count):
    if count <= 5:
        print(count)
        countDown(count + 1)


countDown(1)


#  * Lambda Function - anonymous function (one line)
#  lambda args : logic

sqaure = lambda a: a * a
add = lambda x, y: x + y


evenOdd = lambda x: "Even" if x % 2 == 0 else "Odd"
max = lambda a, b: "A" if a > b else "B"

print(sqaure(5))
print(add(5, 6))

print(evenOdd(70))
print(max(5, 20))

# * array methods
# map , filter , reduce
# map - this will return a new object with all the elements
# filter - will return specific number of elements based on condition
# reduce - will return a single value

num = [1, 2, 3, 4, 5]

res = list(map(lambda x: x * 2, num))
print(res)

res = list(map(lambda x: x * x, num))
print(res)

a = [1, 2, 3]
b = [4, 5, 6]

res = list(map(lambda x, y: x + y, a, b))
print(res)

res = ["Apple", "Banana", "PineApple"]
res = list(map(lambda x: len(x), res))
print(res)

c = [0, 10, 20, 30, 37.777]
f = list(map(lambda x: x * 9 / 5 + 32, c))
print(f)
res = ["Apple", "Anaar", "PineApple"]

cap = list(map(lambda x: x[0], res))

print(cap)



n  =  [1,2,3,4,5]
even = list(filter(lambda x : x % 2 == 0,n))
print(even)
# from functools import reduce

# n = [2, 4, 6, 8, 10, 5]
# even = list(reduce(lambda x: x > 5, n))
# print(even)
