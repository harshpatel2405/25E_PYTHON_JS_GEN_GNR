# print 1 to 4
i = 4
while i >= 1:
    print(i)
    i -= 1

# print sum of 1 to 10
j = 1
n = 10
sum = 0
while j <= n:
    sum += j
    j += 1
print("Sum of 1 to", n, "is", sum)


# prime
# check whether a number is prime or not
#
no = 13
i = 1
count = 0
while i <= no:
    if no % i == 0:
        count += 1
    i += 1

if count == 2:
    print(no, "is prime..")
else:
    print(no, "is not prime..")


str = "Harsh Patel"
i = 0
while i < len(str):
    print(str[i])
    i += 1
