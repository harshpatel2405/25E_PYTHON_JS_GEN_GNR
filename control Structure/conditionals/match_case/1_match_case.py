# match variable:
#     case 1 : 

# No break here

n = 5

match (n):
    case 1 : print("Summer")
    case 2 : print("Monsoon")
    case 3 : print("Winter")
    case 4 : print("Spring")
    case _ : print("Wrong Choice...")

# INDIA        USA
# MUMBAI       New York
# GUJARAT      Chicago

country = int(input("1. India\n2. USA\nEnter Your Choice : "))
match country:
    case 1 : 
            state = int(input("1. MUMBAI\n2. GUJARAT\nEnter Your State : "))
            match state:
                case 1 : print("INDIA  - MUMBAI")
                case 2 : print("INDIA  - GUJARAT")
                case _ : print("INDIA - NO STATE")
    
    case 2 : 
            state = int(input("1. NEW YORK\n2. CHICAGO\nEnter Your State : "))
            match state:
                case 1 : print("USA  - NEW YORK")
                case 2 : print("USA  - CHICAGO")
                case _ : print("INDIA - NO STATE")
    case _ : print("NO COUNTRY SELECTED...")
    