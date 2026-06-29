file = open("data.txt", "r")
x = file.read()

print(file.mode)
print(file.closed)
print(file.name)
print(file.seek(0))
print(file.tell())

file.close()
print(file.closed)