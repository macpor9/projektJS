class BuyProductException(Exception):
    pass

class WrongProductIdException(BuyProductException):
    pass

class NoProductIdException(BuyProductException):
    pass

class ProductNotAvailableException(BuyProductException):
    pass

class NotEnoughMoneyException(BuyProductException):
    pass