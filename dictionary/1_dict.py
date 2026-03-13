info = {"name": "harsh", "age": 21}

print(info)
print(info.keys())
print(info.values())
print(info.items())
print(info.get("name"))

# updating existing and can also add in the data in the existing dictionary
info.update({"age": 122})
info.update({"extra": "name"})
print(info)

info.pop("name")
print(info)


new_dict = info.copy()
print(new_dict)

info.update({"age": 36})
print(new_dict)
print(info)

info.clear()
print(info)


# keys , values , get , items , pop , update , copy , clear ,

# *  Count Frequency of Characters in a String

str = input("Enter a string : ")
print(str)
# # harsh

# freq = {}

# for ch in str:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# for i in freq:
#     print(i, ":", freq[i])

# * Write a program to count frequency of each word in a sentence using a dictionary.
"""
Enter a sentence: python is easy and python is powerful

Word Frequencies:
python : 2
is : 2
easy : 1
and : 1
powerful : 1
"""
str = input("Enter a string : ")
words = str.split()
freq = {}

for ch in words:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for i in freq:
    print(i, ":", freq[i])
