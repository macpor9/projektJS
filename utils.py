from exceptions import WrongNominalException
nominals = [500, 200, 100, 50, 20, 10, 5, 2, 1]

class Coin:
    """
    A class used to represent a Coin

    ...

    Attributes
    ----------
    __value : int
        the value of the coin

    Methods
    -------
    getValue()
        returns the value of the coin
    """
    def __init__(self, value):
        """
        :param value: the value of the coin
        """
        self.__value = value
        if not value in nominals:
            raise WrongNominalException()

    def __str__(self):
        return "{:0.2f}ZL".format(self.__value / 100)

    def __repr__(self):
        return self.__str__()

    def getValue(self):
        """
        :return: the value of the coin
        """
        return self.__value


class Wallet:
    """
    A class used to represent a Wallet, containter for coins

    ...

    Attributes
    ----------
    __coins : list
        a list of coins in wallet
    __nominals : list
        a list of available nominals for coins
    __index : int
        variable needed to make Wallet iterable

    Methods
    -------
    addMoney(coin):
        adds specified coin to the wallet
    addMoneyByValue(value)
        adds to the wallet coin with specified value
    sum()
        returns value of all coins in the wallet
    deleteByCoinValue(value)
        deletes from the wallet a single coin with specified value
    certainCoinValueCount(value)
        returns a number of coins with specified value in the wallet
    clearWallet(self):
        deletes all the coins from wallet
    """
    def __init__(self,moneyValuesList = []):
        """
        :param moneyValuesList: list of values of coins to add to the wallet
        """
        self.__coins = [Coin(x) for x in moneyValuesList]
        self.__nominals = nominals
        self.__index  = len(self.__coins)

    def addMoney(self, coin):
        """
        :param coin: coin to be added to the wallet
        """
        if isinstance(coin, Coin):
            if coin.getValue() in self.__nominals:
                self.__coins.append(coin)
                self.__index+=1
            else:
                raise WrongNominalException()

    def addMoneyByValue(self,value):
        """
        :param value: value of coin to be added to the wallet
        """
        self.addMoney(Coin(value))

    def sum(self):
        """
        :return: value of all coins in the wallet
        """
        suma = 0
        for m in self.__coins:
            suma += m.getValue()
        return suma

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == 0:
            raise StopIteration
        self.__index-=1
        return self.__coins[self.__index]

    def deleteByCoinValue(self,value):
        """
        :param value: value of coin to be deleted from the wallet
        """
        for c in self.__coins:
            if c.getValue() == value:
                self.__coins.remove(c)
                break

    def certainCoinValueCount(self,value):
        """
        :param value: value of coins number to be returned
        :return: a number of coins with specified value in the wallet
        """
        suma = 0
        for c in self.__coins:
            if c.getValue() == value:
                suma+=1
        return suma

    def clearWallet(self):
        self.__coins.clear()
        for n in self.__coins:
            print(f"ss{n}")