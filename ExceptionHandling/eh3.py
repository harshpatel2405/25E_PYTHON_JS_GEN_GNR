class MyException(Exception):
    pass


try:
    password = input("Enter password : ")
    if (len(password) < 8):
        raise MyException("Length of password should be greater than 8")

    print("Password accepted successfully")
except MyException as e:
    print(e)
