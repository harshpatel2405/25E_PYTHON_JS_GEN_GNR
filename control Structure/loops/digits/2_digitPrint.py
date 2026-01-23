n = int(input("Enter a number : "))
temp = n

while(n > 0):
    ld = n % 10 #It will return remainder   132 % 10 = 2
    print(ld)
    n //= 10 # 132 // 10 = 13