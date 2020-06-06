from logic import Automat
from exceptions import *


automat = Automat()


print("------------------------test1------------------------")
price35 = automat.getProductByID(35).getPrice()/100
print(f"cena towaru o numerze 35: {price35}ZL")


print("\n\n------------------------test2------------------------")
automat.addMoney(200)
automat.addMoney(50)
print(f"przed zakupem: {automat.getProductByID(35)}")
print(f"wplacono {automat.getAddedMoney()/100}ZL, zakupiono towar o nr 35 i cenie {price35}ZL , ",end="")
automat.buyProduct(35)
print(f"po zakupie:    {automat.getProductByID(35)}")


print("\n\n------------------------test3------------------------")
automat.addMoney(500)
print(f"przed zakupem: {automat.getProductByID(35)}")
print(f"wplacono {automat.getAddedMoney()/100}ZL, zakupiono towar o nr 35 i cenie {price35}ZL , ",end="")
automat.buyProduct(35)
print(f"po zakupie:    {automat.getProductByID(35)}")



print("\n\n------------------------test4------------------------")
for i in range(6):
    automat.addMoney(500)
    try:
        print(f"przed zakupem: {automat.getProductByID(50)}")
        automat.buyProduct(50)
    except ProductNotAvailableException:
        print("produkt niedostepny")


print("\n\n------------------------test5------------------------")
try:
    price54 = automat.getProductByID(54).getPrice() / 100
    print(f"cena towaru o numerze 35: {price54}ZL")
except WrongProductIdException:
    print("zly numer produktu")


print("\n\n------------------------test6------------------------")
automat.addMoney(200)
automat.addMoney(100)
print(f"suma wrzuconych monet przed przerwaniem transakcji = {automat.getAddedMoney()/100}ZL")
automat.calculateChange()
print(f"suma wrzuconych monet po przerwaniu transakcji = {automat.getAddedMoney()/100}ZL")


print("\n\n------------------------test7------------------------")
automat.addMoney(200)
print(f"test kupowania produktu {automat.getProductByID(32)}")
try:
    print(f"lacznie wrzucono {automat.getAddedMoney()/100}ZL")
    automat.buyProduct(32)
except NotEnoughMoneyException:
    print("niewystarczajaca liczba monet")
automat.addMoney(50)
try:
    print(f"lacznie wrzucono {automat.getAddedMoney() / 100}ZL")
    automat.buyProduct(32)
except NotEnoughMoneyException:
    print("niewystarczajaca liczba monet")


print("\n\n------------------------test8------------------------")
for i in range(400):
    automat.addMoney(1)
print(f"test kupowania produktu {automat.getProductByID(44)}")
print(f"po wrzuceniu 400 razy po 0.01zl, co daje lacznie {automat.getAddedMoney()}")
automat.buyProduct(44)
print(f"stan produktu po kupieniu = {automat.getProductByID(44)}")