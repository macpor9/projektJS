from utils import *
from exceptions import *
class Product:
    """
    A class used to represent a Product

    ...

    Attributes
    ----------
    __name : str
        name of the product
    __count : int
        number of remaining products
    __price : int
        the price of product

    Methods
    -------
    getCount()
        returns the number of remaining products
    getPrice()
        returns the price of product
    setCount(count)
        sets private variable __count to specified value
    setPrice(price)
        sets private variable __price to specified value
    """

    def __init__(self,name,count,price):
        """
        :param name: name of the product represented by class
        :param count: number of remaining products
        :param price: the price of product
        """
        self.__name = name
        self.__count = count
        self.__price = price

    def getCount(self):
        """
        :return: the number of remaining products
        """
        return self.__count

    def getPrice(self):
        """
        :return: the price of product
        """
        return self.__price

    def setCount(self,count):
        """
        :param count: number of remaining products
        """
        self.__count = count

    def setPrice(self,price):
        """
        :param price: the price of product
        """
        self.__price = price

    def __str__(self):
        return f"{self.__name} price: {self.__price/100} count: {self.__count}"

    def __repr__(self):
        return self.__str__()

class Automat:
    """
    A class used to represent an Automat

    ...

    Attributes
    ----------
    __addedMoney : int
        the amount of money added by customer
    __machineWallet : utils.Wallet
        a wallet that contains all the coins excluding the ones from current transaction
    __userAddedWallet : utils.Wallet
        a wallet that contains all the coins added in current transaction
    __products : dict
        a dictionary that contains products and their numbers in automat

    Methods
    -------
    addMoney(moneyValue)
        adds Coin with value specified by 'moneyValue' variable
    valueOfMachineMoney()
        returns value of all money in the automat
    getProductByID(id)
        returns product with specified id
    calculateChange()
        calculates the change after buying product
    getAddedMoney()
        returns the amount of money added by customer in current transaction
    buyProduct(id)
        used to buy product with specified id
    """
    def __init__(self):
        self.__addedMoney = 0
        self.__machineWallet = Wallet([x for x in nominals for j in range(5)])
        self.__userAddedWallet = Wallet()
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
        """
        :param moneyValue: represents money value to be add to the wallet
        """
        self.__userAddedWallet.addMoneyByValue(moneyValue)
        self.__addedMoney = self.__userAddedWallet.sum()

    def valueOfMachineMoney(self):
        """
        :return: value of all money in the automat
        """
        return self.__machineWallet.sum()

    def getProductByID(self,id):
        """
        :param id: id of product to be returned
        :return: product with specified id
        """
        if id not in self.__products.keys():
            raise WrongProductIdException
        return self.__products[id]

    def calculateChange(self):
        """
        :return: the amount of change after transaction
        """
        change = f"reszta = {self.__addedMoney/100}ZL"
        while self.__addedMoney>0:
            n = 0
            for nominal in nominals:
                if self.__machineWallet.certainCoinValueCount(nominal)>0:
                    if self.__addedMoney >= nominal > n:
                        n = nominal
            self.__addedMoney-=n
            self.__machineWallet.deleteByCoinValue(n)
            if self.valueOfMachineMoney()<=0 and self.__addedMoney>0:
                raise CantGiveTheChangeException
        for m in self.__userAddedWallet:
            self.__machineWallet.addMoney(m)
        self.__userAddedWallet.clearWallet()
        return change

    def getAddedMoney(self):
        """
        :return: the amount of money added by customer in current transaction
        """
        return self.__addedMoney

    def buyProduct(self, id):
        """
        :param id: number of product to be bought
        :return: the amount of money added by customer in current transaction
        """
        if id not in self.__products.keys():
            raise WrongProductIdException()
        elif self.__addedMoney<self.getProductByID(id).getPrice():
            raise NotEnoughMoneyException()
        elif self.getProductByID(id).getCount()<=0:
            raise ProductNotAvailableException
        else:
            self.__addedMoney-=self.getProductByID(id).getPrice()
            self.getProductByID(id).setCount(self.getProductByID(id).getCount()-1)
            change = self.calculateChange()
            return change
