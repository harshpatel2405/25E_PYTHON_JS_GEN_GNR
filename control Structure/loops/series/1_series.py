#  1 - x²/2! + x⁴/4! - x⁶/6! + ... up to n term
#  k=0
#  x^0 / 0! = 1 / 1 = 1
"""
X : 2
N : 3

Answer : -0.3333
"""
import math

n = int(input("Enter a number : "))
x = int(input("Enter value of x : "))
ans = 1
sign = -1

for i in range(1, n + 1):
    power = 2 * i
    ans += sign * (x ** (power)) / math.factorial(power)
    sign = sign * -1

print(ans)

# def factorial(n):
#     mul = 1
#     for i in range(1, n + 1):
#         mul *= i
#     return mul
