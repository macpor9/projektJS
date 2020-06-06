class BuyProductException(Exception):
    """ Signal the problem with buying product """
    pass

class WrongProductIdException(BuyProductException):
    """ Signal that choosen product id is wrong """
    pass

class NoProductIdException(BuyProductException):
    """ Signal that product id was not choosen """
    pass

class ProductNotAvailableException(BuyProductException):
    """ Signal the product is not available """
    pass

class NotEnoughMoneyException(BuyProductException):
    """ Signal that there is not enough money added to buy product """
    pass

class CantGiveTheChangeException(Exception):
    """ Signal that automat cant give the change """
    pass

class  WrongNominalException(Exception):
    """ Signal that you cant create coin with such nominal """
    pass