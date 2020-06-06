from utils import *
from exceptions import *
class Product:
    def __init__(self,name,count,price):
        self.__name = name
        self.__count = count
        self.__price = price

    def getName(self):
        return self.__name

    def getCount(self):
        return self.__count

    def getPrice(self):
        return self.__price

    def setName(self,name):
        self.__name = name

    def setCount(self,count):
        self.__count = count

    def setPrice(self,price):
        self.__price = price

    def __str__(self):
        return "{} price: {} count: {}".format(self.__name, self.__price, self.__count)

    def __repr__(self):
        return self.__str__()

class Automat:
    def __init__(self):
        self.__addedMoney = 0
        self.machineWallet = Wallet([x for x in nominals for j in range(5)])
        self.userAddedWallet = Wallet()
        self.__products = {30:Product("Fanta",5,250),
                         31:Product("Coca-cola",5,250),
                         32:Product("Sprite",5,250),
                         33:Product("Mountain-Dew",5,250),
                         34:Product("Mirinda",5,250),
                         35:Product("Pepsi",5,250),
                         36:Product("7-UP",5,250),
                         37:Product("Woda Zywiec Zdroj",5,200),
                         38:Product("Tymbark jablko mieta 0.5L",5,350),
                         39:Product("Tymbark jablko brzoskwinia 0.5L",5,350),
                         40:Product("Tymbark pomarancza brzoskwinia 0.5L",5,350),
                         41:Product("Tiger",5,300),
                         42:Product("Black",5,300),
                         43:Product("Oshee blue 0.5L",5,400),
                         44:Product("Oshee red 0.5L",5,400),
                         45:Product("Oshee yellow 0.5L",5,400),
                         46:Product("Lipton ice tea",5,300),
                         47:Product("Oshee blue 0.5L ZERO", 5, 400),
                         48:Product("Oshee red 0.5L ZERO", 5, 400),
                         49:Product("Oshee yellow 0.5L ZERO", 5, 400),
                         50:Product("Lipton ice tea ZERO", 5, 300),
                         }


    def addMoney(self,moneyValue):
        # print(f"wrzucono {moneyValue/100}ZL")
        self.userAddedWallet.addMoneyByValue(moneyValue)
        self.__addedMoney = self.userAddedWallet.sum()

    def valueOfAllMoney(self):
        retval = self.userAddedWallet.sum() + self.machineWallet.sum()
        return retval

    def getProductByID(self,id):
        return self.__products[id]


    def calculateChange(self):
        print(f"reszta = {self.__addedMoney/100}ZL")
        while self.__addedMoney>0:
            n = 0
            for nominal in nominals:
                if self.machineWallet.certainCoinValueCount(nominal)>0:
                    if self.__addedMoney >= nominal > n:
                        n = nominal
            self.__addedMoney-=n
            self.machineWallet.deleteByCoinValue(n)
            if self.valueOfAllMoney()<=0 and self.__addedMoney>0:
                print("nie mozna wydac reszty")
        for m in self.userAddedWallet.coins:
            self.machineWallet.addMoney(m)
        self.userAddedWallet.coins.clear()

    def getAddedMoney(self):
        return self.__addedMoney



    def buyProduct(self, id):
        if id not in self.__products.keys():
            raise WrongProductIdException()
        if self.__addedMoney<self.getProductByID(id).getPrice():
            raise NotEnoughMoneyException()
        if self.getProductByID(id).getCount()<=0:
            raise ProductNotAvailableException
        self.__addedMoney-=self.getProductByID(id).getPrice()
        self.getProductByID(id).setCount(self.getProductByID(id).getCount()-1)
        self.calculateChange()


def cantGiveTheChange():
    print("tylko odliczona kwota")

def productNotAvailable():
    print("product not available")

def viewTransaction():
    print("kupiono produkt: ")


