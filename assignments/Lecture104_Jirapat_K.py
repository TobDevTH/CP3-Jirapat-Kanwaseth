class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to", self.name, self.lastName, "'s cart")

customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer4 = Customer()

customer1.name = "Jirapat"
customer1.lastName = "K"
customer1.age = 25
customer2.name = "Kanthita"
customer2.lastName = "N"
customer2.age = 23
customer3.name = "Athisthan"
customer3.lastName = "Y"
customer3.age = 25
customer4.name = "Waris"
customer4.lastName = "W"
customer4.age = 24

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()