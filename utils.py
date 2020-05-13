nominals = {500, 200, 100, 50, 20, 10, 5, 2, 1}

class  WrongNominalException(Exception):
    pass

class Coin:
    def __init__(self, value):
        self.value = value
        if not value in nominals:
            raise WrongNominalException()

    def __str__(self):
        return "{:0.2f}ZL".format(self.value)

    def __repr__(self):
        return self.__str__()

    def getValue(self):
        return self.value


class Wallet:
    def __init__(self, nominals):
        self.coins = []
        self.nominals = nominals

    def addMoney(self, moneta):
        if isinstance(moneta, Coin):
            if moneta.getValue() in self.nominals:
                self.coins.append(moneta)
            else:
                raise WrongNominalException()

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