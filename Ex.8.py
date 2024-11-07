userNameInput = input("Username :")
passWordInput = input("Password :")
if userNameInput == "t" and passWordInput == "t1" :
    print("    Welcome to Small Spacet")
    print("1. To ORDER ")
    print("2. For PICK UP ")
    customerInput = input("Type here >> ")
    if customerInput == "1":
        print("------------------------------------------")
        print("               To ORDER")
        print("------------------------------------------")
        print("1. Lime Honey Soda                  30 THB")
        print("2. Cocao                            30 THB")
        print("3. Green Tea                        30 THB")
        customerSelect = input("Can I get >>")
        if customerSelect == "1" or "2" or "3":
            amountInput = int(input("Amount >>"))
            print("Total :", 30*amountInput, "THB" )
    else:
        print("For PICK UP ")
        print("Enter your number order")
        customerNumberOrder = input("Number Order :")
else:
    print("ERROR")