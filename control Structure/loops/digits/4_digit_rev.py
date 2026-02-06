n = int(input("Enter a number : "))

rev = 0
while n > 0:
    ld = n % 10 #* last digit of the number
    rev = rev * 10 + ld #* Reverse Logic
    n //=10 #* floor division

print(rev)