def factorial(n):
    if(n == 0 or n == 1): # * back condition
        return 1

    return n * factorial(n-1)

ans = factorial(2)
print(ans)

