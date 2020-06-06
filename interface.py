import tkinter as tk
import logic
from exceptions import *

class Application(tk.Frame):

    def __init__(self, master=None, automat = logic.Automat()):
        super().__init__(master)
        self.automat = automat
        self.addedMoneyNumber = 0
        self.choosenProductNumber = ""
        self.canvas = tk.Canvas(master,width = 600, height = 500, bg = 'pink')
        self.nominals = [1,2,5,10,20,50,100,200,500]
        self.moneyButtons = [tk.Button(self.canvas, text = str(x/100)+"zl", fg = 'black', bg = 'cornflowerblue',activebackground = 'cornflowerblue',command = lambda x=x: self.moneyButtonFun(x)) for x in self.nominals]
        self.productNumberButtons = [tk.Button(self.canvas, text = x, fg = 'black', bg = 'cornflowerblue',activebackground = 'cornflowerblue',command = lambda x=x: self.productNumberButtonFun(x)) for x in range(0,10)]
        self.cancelButton = tk.Button(self.canvas, text = "cancel", fg = 'black', bg = 'cornflowerblue',activebackground = 'cornflowerblue', command = lambda: self.cancelButtonFun())
        self.buyButton = tk.Button(self.canvas, text = "buy", fg = 'black', bg = 'cornflowerblue',activebackground = 'cornflowerblue', command = lambda: self.buyButtonFun())
        self.addedMoney = tk.Label(master, text = f"wrzucono       ", fg ='black', font = ("Helvetica", 16), bg = 'cornflowerblue', anchor = tk.W)
        self.choosenProduct = tk.Label(master, text = f"wybrany nr:    {self.choosenProductNumber}" , fg ='black', font = ("Helvetica", 16), bg = 'cornflowerblue', anchor = tk.W)
        self.screen = tk.Label(master,bg = 'cornflowerblue')
        self.viewProductInfoText = ""
        self.viewProductInfo = tk.Label(master, text = self.viewProductInfoText,font = ("Helvetica", 13), fg = 'black', bg = 'cornflowerblue')
        self.pack()
        self.create_widgets()

    def refreshTextLabels(self):
        self.addedMoney['text'] = f"wrzucono      {str(self.addedMoneyNumber / 100)} zl"
        self.choosenProduct['text'] = f"wybrany nr:    {self.choosenProductNumber}"
        self.viewProductInfo['text'] = self.viewProductInfoText

    def moneyButtonFun(self,amount):
        self.automat.addMoney(amount)
        self.addedMoneyNumber+=amount
        self.refreshTextLabels()

    def productNumberButtonFun(self,number):
        if len(self.choosenProductNumber)<2:
            self.choosenProductNumber+=str(number)
        self.refreshTextLabels()

    def cancelButtonFun(self):
        self.addedMoneyNumber = 0
        self.choosenProductNumber = ""
        self.refreshTextLabels()
        self.automat.calculateChange()


    def buyButtonFun(self):
        try:
            if len(self.choosenProductNumber)<1:
                raise NoProductIdException()
            change = self.automat.buyProduct(int(self.choosenProductNumber))
            self.viewProductInfoText = change
            self.addedMoneyNumber = 0
            self.choosenProductNumber = ""
            self.refreshTextLabels()
        except WrongProductIdException:
            self.viewProductInfoText = "zly numer produktu"
            self.choosenProductNumber = ""
        except NoProductIdException:
            self.viewProductInfoText = "wybierz numer produktu"
        except ProductNotAvailableException:
            self.viewProductInfoText = "produkt niedostepny"
        except NotEnoughMoneyException:
            self.viewProductInfoText = "niewystarczajaca liczba monet"

        self.refreshTextLabels()


    def create_widgets(self):
        self.addedMoney.pack()
        self.choosenProduct.pack()
        width = float(self.canvas['width'])
        mnbtX,mnbtY = 75,200
        pnbtX,pnbtY = 345,200
        for i in range(9):
            self.moneyButtons[i].place(x =mnbtX+i%3*width/10, y = mnbtY+i//3*50,width = 50, height = 30 )
            self.productNumberButtons[i + 1].place(x =pnbtX+i%3*width/10, y = pnbtY+i//3*50,width = 50, height = 30 )
        self.productNumberButtons[0].place(x =pnbtX+60, y = pnbtY+150,width = 50, height = 30 )
        self.addedMoney.place(x = 50,y = 90,width = 250, height = 40)
        self.choosenProduct.place(x = 50, y = 50, width = 250, height = 40)
        self.cancelButton.place(x = mnbtX,y = mnbtY+150,width = 50, height = 30)
        self.buyButton.place(x = mnbtX+120, y = mnbtY+150, width = 50, height = 30)
        self.screen.place(x = 300,y = 50, width = 250, height = 80)
        self.viewProductInfo.place(x = 300, y = 50, width = 250, height = 80)

        self.canvas.pack()


root = tk.Tk()
root.title("Automat")
app = Application(master=root)
app.mainloop()
