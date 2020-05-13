import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None,):
        super().__init__(master)
        self.addedMoneyNumber = 0
        self.choosenProductNumber = ""
        self.canvas = tk.Canvas(master,width = 600, height = 800, bg = 'pink')
        self.nominals = [1,2,5,10,20,50,100,200,500]
        self.moneyButtons = [tk.Button(self.canvas, text = str(x/100)+"zl", fg = 'red', bg = 'blue') for x in self.nominals]
        self.productNumberButtons = [tk.Button(self.canvas, text = x, fg = 'red', bg = 'blue') for x in range(0,10)]
        self.cancelButton = tk.Button(self.canvas, text = "get money back", fg = 'red', bg = 'blue')
        self.addedMoney = tk.Label(master, text = "wrzucono           " + str(self.addedMoneyNumber / 100) + "zl", fg ='green', font = ("Helvetica", 16), bg = 'pink', anchor = tk.W)
        self.choosenProduct = tk.Label(master, text = "wybrany numer:  0" + self.choosenProductNumber, fg ='green', font = ("Helvetica", 16), bg = 'pink', anchor = tk.W)
        self.master = master
        self.pack()
        self.create_widgets()

    #     self.moneyButtonLogic = None
    #     self.productNumberButtonLogic = None
    #     self.cancelButtonlogic= None
    #
    #
    # def setFuncitons(self,moneyButtonLogic,productNumberButtonLogic,cancelButtonLogic ):
    #     self.moneyButtonLogic = moneyButtonLogic
    #     self.productNumberButtonLogic = productNumberButtonLogic
    #     self.cancelButtonlogic = cancelButtonLogic

    def refreshTextLabels(self):
        self.addedMoney['text'] = "wrzucono           " + str(self.addedMoneyNumber / 100) + "zl"
        self.choosenProduct['text'] = "wybrany numer:  " + self.choosenProductNumber

    def moneyButtonFun(self,amount):
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


    def create_widgets(self):
        self.addedMoney.pack()
        self.choosenProduct.pack()
        width = float(self.canvas['width'])


        for i in range(9):
            mnbtX,mnbtY = 75,300
            pnbtX,pnbtY = 345,300
            self.moneyButtons[i].place(x =mnbtX+i//3*width/10, y = mnbtY+i%3*50,width = 50, height = 30 )
            print(mnbtX+i//3*width/10, mnbtY+i%3*50)
            self.productNumberButtons[i + 1].place(x =pnbtX+i//3*width/10, y = pnbtY+i%3*50,width = 50, height = 30 )
        self.productNumberButtons[0].place(x =405, y = 450,width = 50, height = 30 )
        self.addedMoney.place(x = 50,y = 100,width = 250, height = 30)
        self.choosenProduct.place(x = 50, y = 50, width = 250, height = 30)

        self.cancelButton.place(x = 110,y = 450,width = 100, height = 30)

        for n in self.nominals:
            self.moneyButtons[self.nominals.index(n)]['command'] = lambda n=n: self.moneyButtonFun(n)
            self.productNumberButtons[self.nominals.index(n)]['command'] = lambda n=n: self.productNumberButtonFun(self.nominals.index(n))
        self.cancelButton['command'] = lambda n=n: self.cancelButtonFun()




        self.canvas.pack()



# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()