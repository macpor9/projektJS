class Product():
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


class Automat():
    def __init__(self):
        self.__moneys = {1: 0, 2: 0, 5:0, 10:0, 20:0, 50:0, 100:0, 200:0, 500:0}
        self.__products = {30:Product("Fanta",10,250),
                         31:Product("Coca-cola",10,250),
                         32:Product("Sprite",10,250),
                         33:Product("Mountain-Dew",10,250),
                         34:Product("Mirinda",10,250),
                         35:Product("Pepsi",10,250),
                         36:Product("7-UP",10,250),
                         37:Product("Woda Zywiec Zdroj",10,200),
                         38:Product("Tymbark jablko mieta 0.5L",7,350),
                         39:Product("Tymbark jablko brzoskwinia 0.5L",7,350),
                         40:Product("Tymbark pomarancza brzoskwinia 0.5L",7,350),
                         41:Product("Tiger",10,300),
                         42:Product("Black",10,300),
                         43:Product("Oshee blue 0.5L",5,400),
                         44:Product("Oshee red 0.5L",5,400),
                         45:Product("Oshee yellow 0.5L",5,400),
                         46:Product("Lipton ice tea",10,300),
                         47:Product("Oshee blue 0.5L ZERO", 5, 400),
                         48:Product("Oshee red 0.5L ZERO", 5, 400),
                         49:Product("Oshee yellow 0.5L ZERO", 5, 400),
                         50:Product("Lipton ice tea ZERO", 10, 300),
                         }

    def addMoney(self,moneyValue):
        self.__moneys[moneyValue]+=1

    def paidAmout(self):
        retval = 0
        for k,v in self.__moneys.items():
            retval+=k*v
        return retval

    def getProductByID(self,id):
        return self.__products[id]

a = Automat()
print(a.getProductByID(35))
a.addMoney(200)
a.addMoney(500)
a.addMoney(20)
print("paid amount",a.paidAmout())