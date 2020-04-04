username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "1234":
    print("------Welcome Pie Shop------")
    print("----------------------------")
    print("1. Apple Pie     = 100 (Bath)")
    print("2. Orange Pie    = 120 (Bath)")
    print("3. Blueberry Pie = 150 (Bath)")
    print("----------------------------")
    select = int(input("Choose your menu (No.) >>"))
    if select == 1:
        print("How many do you want ?")
        unit = int(input(">>"))
        total = unit * 100
        print("Total : ", total, " Bath")
    elif select == 2:
        print("How many do you want ?")
        unit = int(input(">>"))
        total = unit * 120
        print("Total : ", total, " Bath")
    elif select == 3:
        print("How many do you want ?")
        unit = int(input(">>"))
        total = unit * 150
        print("Total : ", total, " Bath")
    else:
        print("Error!!!")
        print("You didn't select an item in the menu.")




