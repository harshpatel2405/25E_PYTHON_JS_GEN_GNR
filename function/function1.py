
#  ^ variable length args
# *args -- this will convert input into tuple
def getSum(*num):
    sum =0
    for i in num :
        print(i)
        sum += i
    print("Sum =",sum)

getSum(10,20,30,40,50)    

# ** kwargs -- it works on key value pairs
def getData(**kwargs):
    print(kwargs)

getData(name = "Harsh", age = 21)
    
# * lambda (anonymous function)
# & lambda args : expression
ans = lambda : print("Hello this is lambda function")
ans()

square = lambda x : x*x
print(square(5))

# * recursive function -- function calling itself
#  ^ it will get into inifinity , if we dont provide a base condition
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)
print(factorial(5))