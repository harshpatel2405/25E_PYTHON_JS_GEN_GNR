file = open("data.txt")

# * complete file read
# print(file.read())
# x = file.read()
# print(x)

# * read lines
lineCount = 0
while True:
    x =file.readline()
    print(x, end = "")

    if not x:
        break
    lineCount+=1

file.close()
print("\nLines :", lineCount)