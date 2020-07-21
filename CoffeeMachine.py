class CoffeeMachine():

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def available(self):
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money")

    def making_cup(self):
        print("I have enough resources, making you a coffee!")


    def buy(self):
        item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if item == "1":
            if self.water <= 250:
                print("Sorry, not enough water!")
            elif self.coffee < 16:
                print("Sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                return self.making_cup()
        elif item == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.coffee < 20:
                print("Sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                return self.making_cup()
        elif item == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.coffee < 12:
                print("Sorry, not enough coffee!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                return self.making_cup()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money -= self.money

    def action_cm(self):
        action = input("Write action (buy, fill, take, remaining, exit): ")
        while action != "exit":
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.available()
            action = input("\nWrite action (buy, fill, take, remaining, exit): ")

order = CoffeeMachine(400, 540, 120, 9, 550)
order.action_cm()
