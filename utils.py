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

    def addMoney(self, moneta):
        if isinstance(moneta, Coin):
            if moneta.getValue() in self.nominals:
                self.coins.append(moneta)
            else:
                raise WrongNominalException()

    def addMoneyByValue(self,value):
        self.addMoney(Coin(value))

    def sum(self):
        sum = 0
        for m in self.coins:
            sum += m.getValue()
        return sum


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

        # self.delete(Coin(value))

    def certainCoinValueCount(self,value):
        sum = 0
        for c in self.coins:
            if c.getValue() == value:
                sum+=1
        return sum

        # return self.coins.count(Coin(value))



# a = Wallet([200,100])
# a.addMoneyByValue(500)
# a.addMoneyByValue(500)
# print(a.sum())
# print(a.coins[1])
# print(a.certainCoinValueCount(500))
#
# c1 = Coin(500)
# c2 = Coin(200)
#
# lista = [c1,c2]
# print(lista.count(Coin(200)))

#
# print("ss")
#
# moneys = Wallet([x for x in nominals for j in range(5)])
# print("dd")
# print(moneys.sum())