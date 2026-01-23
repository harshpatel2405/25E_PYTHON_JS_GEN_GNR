n = int(input("Enter a number : "))
temp = n
sum = 0
mul = 1

while(n > 0):
    ld = n % 10 #It will return remainder   132 % 10 = 2
    sum += ld
    mul *= ld
    n //= 10 # 132 // 10 = 13

print("Sum of digits of",temp,"is",sum)
print("Multiplication of digits of",temp,"is",mul)