price = int(input("Total price : "))
def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * 7 / 100)
    return result

print("Price + Vat = ", vatCalculate(price))

