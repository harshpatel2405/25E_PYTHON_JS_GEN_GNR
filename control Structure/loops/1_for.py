n = int(input("Enter a number : "))

for i in range(1, n):
    print(i)


# check if d is present in any string given by user
str = input("Enter a string : ")
count = 0
for i in str:
    if i == "d" or i == "D":
        count += 1

print("D(d) appeared", count, "times")
