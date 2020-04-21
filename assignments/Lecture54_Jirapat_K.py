def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- Welcome to Shop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

if login() == True:
    showMenu()
    mnSel = 0
    while mnSel != 2 or mnSel != 1:
        mnSel = menuSelect()
        if mnSel == 1:
            totalPrice = float(input("Price : "))
            print("Total price : ", vatCalculate(totalPrice))
            break
        elif mnSel == 2:
            print("Total price : ", priceCalculate())
            break
        else:
            print("Error!!!")
            print("Try again")
else:
    print("Login failed!!!")







