try:
    a = 10
    b = 0
    if (b == 0):
        raise ZeroDivisionError("Do not divide by zero as it leads to infinity")
    print(a/b)
except ZeroDivisionError as e:
    print(e)