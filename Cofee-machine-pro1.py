# create a project on coffee machine which will print that hash images of that specific classes like 
# late, mocha , americano,etc., where coffe is the abstract class and remaineing are the encapsulater
# one which is wraped within the coffee and the reciperice of this could be created using inheritnce properties a,
#write a pyton code to run this coffee code on the terminal
from abc import ABC, abstractmethod

class Coffee(ABC):
    def __init__(self, coffeeType, waterAmount):
        self.__coffeeType = coffeeType
        self.__waterAmount = waterAmount

    def getCoffeeType(self):
        return self.__coffeeType

    def getWaterAmount(self):
        return self.__waterAmount

    @abstractmethod
    def makeCoffee(self):
        pass

    def printArt(self):
        print("Here is your order:")


class Espresso(Coffee):
    def makeCoffee(self):
        return f"Espresso: {self.getCoffeeType()} (strong shot)"


class Americano(Coffee):
    def makeCoffee(self):
        return f"Americano: {self.getCoffeeType()} + {self.getWaterAmount()}"


class Latte(Coffee):
    def __init__(self, coffeeType, waterAmount, milkAmount):
        super().__init__(coffeeType, waterAmount)
        self.__milkAmount = milkAmount

    def getMilkAmount(self):
        return self.__milkAmount

    def makeCoffee(self):
        return f"Latte: {self.getCoffeeType()} + {self.getWaterAmount()} + {self.getMilkAmount()}"


class Cappuccino(Coffee):
    def __init__(self, coffeeType, waterAmount, milkAmount, foamAmount):
        super().__init__(coffeeType, waterAmount)
        self.__milkAmount = milkAmount
        self.__foamAmount = foamAmount

    def makeCoffee(self):
        return f"Cappuccino: {self.getCoffeeType()} + {self.getWaterAmount()} + {self.__milkAmount} + {self.__foamAmount}"


class Mocha(Coffee):
    def __init__(self, coffeeType, waterAmount, chocolateAmount):
        super().__init__(coffeeType, waterAmount)
        self.__chocolateAmount = chocolateAmount

    def makeCoffee(self):
        return f"Mocha: {self.getCoffeeType()} + {self.getWaterAmount()} + {self.__chocolateAmount}"


class Frappe(Coffee):
    def __init__(self, coffeeType, waterAmount, iceAmount):
        super().__init__(coffeeType, waterAmount)
        self.__iceAmount = iceAmount

    def makeCoffee(self):
        return f"Frappe: {self.getCoffeeType()} + {self.getWaterAmount()} + {self.__iceAmount}"


print("\n☕ Welcome to Coffee Machine ☕")
print("1. Espresso")
print("2. Americano")
print("3. Latte")
print("4. Cappuccino")
print("5. Mocha")
print("6. Frappe")

userChoice = int(input("Select your coffee (1-6): "))

if userChoice == 1:
    coffeeOrder = Espresso("Coffee", "No Water")
elif userChoice == 2:
    coffeeOrder = Americano("Coffee", "Water")
elif userChoice == 3:
    coffeeOrder = Latte("Coffee", "Water", "Milk")
elif userChoice == 4:
    coffeeOrder = Cappuccino("Coffee", "Water", "Milk", "Foam")
elif userChoice == 5:
    coffeeOrder = Mocha("Coffee", "Water", "Chocolate")
elif userChoice == 6:
    coffeeOrder = Frappe("Coffee", "Water", "Ice")
else:
    print("Invalid choice!")
    exit()

coffeeOrder.printArt()
print(coffeeOrder.makeCoffee())