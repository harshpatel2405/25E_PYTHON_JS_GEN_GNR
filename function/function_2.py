
#  * nested function 
'''
outer 
  |
  |-- creates inner
  |-- calls inner

'''

def outer():
    print("Outer Function")

    # * creating inner
    def inner():
        print("Inner Function")
    
    # * calling inner
    inner()

#  * calling outer 
outer()

def calculator():
    def add(a,b):
        print(a+b)

    add(10,15)
calculator()


def greeting(name):
    def message():
        print("Welcome ,", name)
    message()
greeting("Harsh")