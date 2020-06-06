nominals = [500, 200, 100, 50, 20, 10, 5, 2, 1]

class  WrongNominalException(Exception):
    pass

class Coin:
    def __init__(self, value):
        self.value = value
        if not value in nominals:
            raise WrongNominalException()

    def __str__(self):
        return "{:0.2f}ZL".format(self.value/100)

    def __repr__(self):
        return self.__str__()

    def getValue(self):
        return self.value




class Wallet:
    def __init__(self,moneyValuesList = []):
        self.coins = [Coin(x) for x in moneyValuesList]
        self.nominals = nominals
        self.__index  = len(self.coins)

    def addMoney(self, moneta):
        if isinstance(moneta, Coin):
            if moneta.getValue() in self.nominals:
                self.coins.append(moneta)
            else:
                raise WrongNominalException()

    def addMoneyByValue(self,value):
        self.addMoney(Coin(value))

    def sum(self):
        suma = 0
        for m in self.coins:
            suma += m.getValue()
        return suma

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == 0:
            raise StopIteration
        self.__index-=1
        return self.coins[self.__index]

    def delete(self, coin):
        for i in self.coins:
            if i.getValue() is coin:
                self.coins.remove(i)
                return i

    def deleteByCoinValue(self,value):
        for c in self.coins:
            if c.getValue() == value:
                self.coins.remove(c)
                break

    def certainCoinValueCount(self,value):
        suma = 0
        for c in self.coins:
            if c.getValue() == value:
                suma+=1
        return suma