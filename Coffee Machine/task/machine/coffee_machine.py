class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money


    def status(self):
        print()
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.money), "of money")


    def buy(self, order):
        #global water, milk, coffee, cups, money
        if order == '1':
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
        if order == '2':
            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
            elif self.water < 350:
                print("sorry, not enough water!")
        if order == '3':
            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
            else:
                print("sorry, not enough", min(self.water, self.milk, self.coffee, self.cups)+"!")
        if order == 'back':
            print()


    def fill(self):
        #global water, milk, coffee, cups
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))


    def active(self):
        print()
        action = input("Write action (buy, fill, take, remaining, exit) :")
        if action == "buy":
            self.buy(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
            self.active()
        if action == "fill":
            self.fill()
            self.active()
        if action == "take":
            print("I gave you $", self.money)
            self.money = 0
            self.active()
        if action == "remaining":
            self.status()
            self.active()
        if action == "exit":
            exit


coffee = CoffeeMachine(400, 540, 120, 9, 550)
active = True
coffee.active()