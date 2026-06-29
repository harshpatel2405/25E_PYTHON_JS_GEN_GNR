
# * Decorators -- decorate (enhance) existing function
# * Gift -- Original function     Ribbon -- Decorator
'''
def decorator(func):
    def wrapper():
        # extra functionlitie
        func()  

    return wrapper
'''


# * program 1
def decor(func):
    def wrap():
        print("Welcome User")
        func()

    return wrap


def greet():
    print("Good Morning")


obj = decor(greet)
obj()


# * program 2
def decorator(function):
    def wrapper():
        print("Login Successfulll")
        function()
        print("Thank you..")

    return wrapper

def dashboard():
    print("Welcome to the dashboard")

obj = decorator(dashboard)
obj()

# * program 3
def decor1Func(function):
    def wrapper():
        print("This is wrapper function")
        function()
        print("Thank You")

    return wrapper

@decor1Func
def check():
    print("This is check function")

check()