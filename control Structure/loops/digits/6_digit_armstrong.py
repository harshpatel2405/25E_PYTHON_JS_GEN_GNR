"""
123 = 1^3 + 2^3 + 3^3 = 123

8196 = 8^4 + 1^4 + 9^4 + 6^4 = 8196
"""

s = input("Enter a number : ")
sum = 0
count = len(s)
n = int(s)
temp = n

while n > 0:
    ld = n % 10
    mul = 1
    for i in range(count):  # starts with 0
        mul *= ld
    sum += mul
    n //= 10
print
if temp == sum:
    print(temp, "is Armstrong Number..")
else:
    print(temp, "is not Armstrong Number..")


'''
1. Harshad Number
2. Digital Root
3. Disarium Number
4. Krishnamurthy Number
'''