
import os
print(os.path.exists("data.txt"))


print(os.path.isfile("data.txt"))
print(os.path.isdir("data.txt"))

print(os.path.getsize("data.txt"))
print(os.path.getctime("data.txt"))

# * if file exists , then file will be deleted
# os.remove("data.txt")

# os.rename("data.txt","demo.txt")
# os.rename("demo.txt","data.txt")

# * will close file itself 
with open("data.txt","r") as file:
    print(file.read())