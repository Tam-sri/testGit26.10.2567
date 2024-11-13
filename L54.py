def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Enter your selection >>"))
    if userSelected == 1:
       return priceCalculate()
    if userSelected == 2:
       return priceCalculate()
    else:
        print("Press 1 or 2 >> Try again")
        menuSelect()

def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    print("Included Vat :", result)
    return result

def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    print("Total Price :", totalPrice)
    return vatCalculate(totalPrice)
print(login())

'''
def login():
    pass
def showMenu():
    pass
def menuSelect():
    pass
def vatCalculator():
    pass
def priceCalculator():
    pass


usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1 + price2)
'''