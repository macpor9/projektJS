import tkinter as tk
import logic
from exceptions import *

class Application(tk.Frame):
    """
    The main class of automat interface

    ...

    Attributes
    ----------
    automat : Automat
        instance of the Automat class, responsible for applicaton logic
    __addedMoneyNumber : int
        the amount of money added by customer
    __choosenProductNumber : str
        selected product number
    __canvas : tkinter.Canvas
        the main canvas of the automat
    __nominals : list
        a list of an available nominals for coins
    __moneyButtons : list
        a list of buttons to add money to the automat
    __productNumberButtons : list
        a list of buttons to choose number of product to buy
    __cancelButton : tkinter.Button
        a button to cancel the transaction and get the money back
    __buyButton : tkinter.Button
        a button to buy product with already choosen number
    __addedMoney : tkinter.Label
        a label to view the amount of added money
    __choosenProduct : tkinter.Label
        a label to view choosen product number
    __viewInfoText : str
        tekst to display on the screen
    __viewInfo : tkinter.Label
        a label to view info about actions taken by customer

    Methods
    -------
    refreshTextLabels()
        refreshes the informations viewed on the screen
    moneyButtonFun(amount)
        adds Coin with value specified by 'amount' variable
    productNumberButtonFun(number)
        changes the number of choosen product and saves it into '__choosenProductNumber' variable
    cancelButtonFun()
        cancels the transaction and refunds all the money to customer
    buyButtonFun()
        used to buy product with already choosen number
    create_widgets()
        places all the labels and buttons on the canvas
    """
    def __init__(self, master=None, automat = logic.Automat()):
        """
        :param master:  represents the parent window
        :param automat: represents the automat that provides logic of the application
        """
        super().__init__(master)
        self.__automat = automat
        self.__addedMoneyNumber = 0
        self.__choosenProductNumber = ""
        self.__canvas = tk.Canvas(master, width = 600, height = 500, bg ='pink')
        self.__nominals = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        self.__moneyButtons = [tk.Button(self.__canvas, text =str(x / 100) + "zl", fg ='black', bg ='cornflowerblue', activebackground ='cornflowerblue', command = lambda x=x: self.moneyButtonFun(x)) for x in self.__nominals]
        self.__productNumberButtons = [tk.Button(self.__canvas, text = x, fg ='black', bg ='cornflowerblue', activebackground ='cornflowerblue', command = lambda x=x: self.productNumberButtonFun(x)) for x in range(0, 10)]
        self.__cancelButton = tk.Button(self.__canvas, text ="cancel", fg ='black', bg ='cornflowerblue', activebackground ='cornflowerblue', command = lambda: self.cancelButtonFun())
        self.__buyButton = tk.Button(self.__canvas, text ="buy", fg ='black', bg ='cornflowerblue', activebackground ='cornflowerblue', command = lambda: self.buyButtonFun())
        self.__addedMoney = tk.Label(master, text =f"wrzucono       ", fg ='black', font = ("Helvetica", 16), bg ='cornflowerblue', anchor = tk.W)
        self.__choosenProduct = tk.Label(master, text =f"wybrany nr:    {self.__choosenProductNumber}", fg ='black', font = ("Helvetica", 16), bg ='cornflowerblue', anchor = tk.W)
        self.__viewInfoText = ""
        self.__viewInfo = tk.Label(master, text = self.__viewInfoText, font = ("Helvetica", 13), fg ='black', bg ='cornflowerblue')
        self.pack()
        self.create_widgets()

    def refreshTextLabels(self):
        self.__addedMoney['text'] = f"wrzucono      {str(self.__addedMoneyNumber / 100)} zl"
        self.__choosenProduct['text'] = f"wybrany nr:    {self.__choosenProductNumber}"
        self.__viewInfo['text'] = self.__viewInfoText

    def moneyButtonFun(self,amount):
        """
        :param amount: amount of monney that will be added to the automat Wallet
        """
        self.__automat.addMoney(amount)
        self.__addedMoneyNumber+=amount
        self.refreshTextLabels()

    def productNumberButtonFun(self,number):
        """
        :param number: number to add to __choosenProductNumber
        """
        if len(self.__choosenProductNumber)<2:
            self.__choosenProductNumber+=str(number)
        self.refreshTextLabels()

    def cancelButtonFun(self):
        self.__addedMoneyNumber = 0
        self.__choosenProductNumber = ""
        try:
            self.__automat.calculateChange()
        except CantGiveTheChangeException:
            pass
        self.refreshTextLabels()


    def buyButtonFun(self):
        try:
            if len(self.__choosenProductNumber)<1:
                raise NoProductIdException()
            change = self.__automat.buyProduct(int(self.__choosenProductNumber))
            self.__viewInfoText = change
            self.__addedMoneyNumber = 0
            self.__choosenProductNumber = ""
            self.refreshTextLabels()
        except WrongProductIdException:
            self.__viewInfoText = "zly numer produktu"
            self.__choosenProductNumber = ""
        except NoProductIdException:
            self.__viewInfoText = "wybierz numer produktu"
        except ProductNotAvailableException:
            self.__viewInfoText = "produkt niedostepny"
        except NotEnoughMoneyException:
            self.__viewInfoText = "niewystarczajaca liczba monet"
        except CantGiveTheChangeException:
            self.__viewInfoText = "nie mozna wydac reszty"

        self.refreshTextLabels()


    def create_widgets(self):
        self.__addedMoney.pack()
        self.__choosenProduct.pack()
        width = float(self.__canvas['width'])
        mnbtX,mnbtY = 75,200
        pnbtX,pnbtY = 345,200
        for i in range(9):
            self.__moneyButtons[i].place(x =mnbtX + i % 3 * width / 10, y =mnbtY + i // 3 * 50, width = 50, height = 30)
            self.__productNumberButtons[i + 1].place(x =pnbtX + i % 3 * width / 10, y =pnbtY + i // 3 * 50, width = 50, height = 30)
        self.__productNumberButtons[0].place(x =pnbtX + 60, y =pnbtY + 150, width = 50, height = 30)
        self.__addedMoney.place(x = 50, y = 90, width = 250, height = 40)
        self.__choosenProduct.place(x = 50, y = 50, width = 250, height = 40)
        self.__cancelButton.place(x = mnbtX, y =mnbtY + 150, width = 50, height = 30)
        self.__buyButton.place(x =mnbtX + 120, y =mnbtY + 150, width = 50, height = 30)
        self.__viewInfo.place(x = 300, y = 50, width = 250, height = 80)

        self.__canvas.pack()


root = tk.Tk()
root.title("Automat - Maciej Poreba lab06")
app = Application(master=root)
app.mainloop()
