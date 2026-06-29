'''
Problem: Simple Bank Withdrawal System

Requirements:
    Initial account balance is ₹10,000.
    Ask the user to enter the withdrawal amount.
    Use try-except-else-finally blocks.
    If the user enters a non-numeric value, handle it using ValueError.
    If the withdrawal amount is negative or zero, manually raise a ValueError using raise.
    If the withdrawal amount is greater than the account balance, manually raise an exception with a suitable message.
    If no exception occurs:
        Deduct the amount from the balance.
    Display the remaining balance.
Use the finally block to print:
    Thank you for using our banking system.
'''
balance = 10000
try:
    withdrawlAmount = int(input("Enter amount : "))
    
    if(withdrawlAmount <= 0):
        raise ValueError("Withdrawl amount should be greater than 0")
    
    if(withdrawlAmount > balance):
        raise Exception("Withdrawl amount should be less than balance")

except ValueError as e:
    print("Error :",e)
except Exception as e:
    print("Error :",e)
else:
    balance -= withdrawlAmount
    print("Amount withdrawn :", withdrawlAmount)
    print("Current Balance :", balance)
finally:
    print("hank you for using our banking system.")

