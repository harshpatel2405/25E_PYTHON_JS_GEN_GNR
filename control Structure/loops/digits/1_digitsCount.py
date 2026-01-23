n = int(input("Enter a number : "))
temp = n
count = 0
while n > 0:
    count += 1
    n //= 10

# Number of digits in 1234 is 4
print("Number of digits in", temp, "is", count)
