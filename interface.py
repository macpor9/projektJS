import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None,):
        super().__init__(master)
        self.addedMoneyNumber = 0
        self.choosenProductNumber = ""
        self.canvas = tk.Canvas(root,width = 640, height = 640)
        self.nominals = [1,2,5,10,20,50,100,200,500]
        self.moneyButtons = [tk.Button(self.canvas, text = str(x/100)+"zl",width = 10) for x in self.nominals]
        self.productNumberButtons = [tk.Button(self.canvas, text = x, width = 10) for x in range(0,10)]
        self.addedMoney = tk.Label(root, text = "wrzucono " + str(self.addedMoneyNumber / 100) + "zl", fg ='green', font = ("Helvetica", 16))
        self.choosenProduct = tk.Label(root, text = "wybrany numer: " + self.choosenProductNumber, fg ='green', font = ("Helvetica", 16))
        self.master = master
        self.pack()
        self.create_widgets()



    def refreshTextLabels(self):
        self.addedMoney['text'] = "wrzucono " + str(self.addedMoneyNumber / 100) + "zl"
        self.choosenProduct['text'] = "wybrany numer: " + self.choosenProductNumber

    def moneyButtonFun(self,amount):
        self.addedMoneyNumber+=amount
        self.refreshTextLabels()

    def productNumberButtonFun(self,number):
        self.choosenProductNumber+=str(number)
        self.refreshTextLabels()


    def create_widgets(self):
        self.addedMoney.pack()
        self.choosenProduct.pack()

        for i in range(9):
            self.moneyButtons[i].grid(row = i//3, column = i%3)
            self.productNumberButtons[i].grid(row=i // 3+3, column=i % 3)

        for n in self.nominals:
            self.moneyButtons[self.nominals.index(n)]['command'] = lambda n=n: self.moneyButtonFun(n)
            self.productNumberButtons[self.nominals.index(n)]['command'] = lambda n=n: self.productNumberButtonFun(self.nominals.index(n))





        self.canvas.pack()



root = tk.Tk()
app = Application(master=root)
app.mainloop()