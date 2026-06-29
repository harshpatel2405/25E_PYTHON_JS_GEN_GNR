
# * Higher Order Function
'''
1. Accepts function as an argument 
2. returns function
'''


# * accepting function as args
def greet():
    print("Good Morning")


def welcome(fun):
    print("Inside welcome function")
    fun()


welcome(greet)


def expo(n):
    return n*n

def calculate(func , value):
    result = func(value)
    print("Result :", result)

calculate(expo, 10)

# * return another function
def outer():
    print("Welcome to outer function")

    def inner():
        print("Welcome to inner function")

    return inner



obj = outer()
obj()