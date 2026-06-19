try:
    a = int(input("Enter a number: "))
    a = 10
    b = 10
    print(a/b)
except ZeroDivisionError:
    print("Error : Divide by Zero")
except ValueError:
    print("Data type mismatch")
else:
    print("run if no error")
finally:
    print("Always gets executed")

print("Rest of the program")
