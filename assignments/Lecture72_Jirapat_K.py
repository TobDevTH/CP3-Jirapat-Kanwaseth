menuList = []

def showBill():
    print("---- My Food ----")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0], ":", menuList[number][1], "THB")
        total += menuList[number][1]
    print("Total :", total, "THB")

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName, menuPrice])


showBill()

