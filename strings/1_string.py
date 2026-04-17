# * string is immutable

name = "Ram"
name = "Shyam"

str = "This is Sample String"

# index
print(str[1])

# slice
print(str[0:5])
print(str[:15])
print(name[::2])  # skips 2 (starts from 0)
print(name[1::2])  # skips 2 (starts from 1)

# case change
print(name.capitalize())
print(str.lower())
print(str.upper())

# strip (removes extra whitesapce before and after string)
greet = "    hi     "
print(greet.strip())

# replace
text = "Hello World"
print(text.replace("World", "Python"))


# find and count 
s = 'Apple Banana'
print(s.count("a"))
print(s.find("B"))

#reverse
print(name[::-1])

# loop printing
s = 'Hello'
for i in s:
    print(i , end = "")