menuList = []
priceList = []

def showBill():
    print("---- My Food ----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total += priceList[number]
    print("Total :", total)

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()


