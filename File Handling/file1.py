file = open("./data.txt", "a")

# *  will store in single line
# file.write("This is my first line of file handling\n")
a = 42
# file.write(f"My age is {a}\n")

# # will store in different lines
# file.writelines("This is second line\n")
# file.writelines("This is third line")

# lines = ['java\n', 'c++\n', 'python\n', 'dsa\n']
# file.writelines(lines)

file.close()
