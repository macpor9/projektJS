import tkinter as tk
from PIL import ImageTk,Image

class Application(tk.Frame):
    moneyButtons = []

    def __init__(self, master=None,):
        super().__init__(master)
        # self.vendingMachineImage = ImageTk.PhotoImage(Image.open("images/vendingmachine.jpg"))
        self.canvas = tk.Canvas(root,width = 640, height = 640, bg = 'red')
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.canvas.create_image(320,320,image = self.vendingMachineImage)
        self.moneyButtons.append(tk.Button(root,text = "1gr"))
        self.moneyButtons.append(tk.Button(root,text = "2gr"))
        self.moneyButtons.append(tk.Button(root,text = "5gr"))
        self.moneyButtons.append(tk.Button(root,text = "10gr"))
        self.moneyButtons.append(tk.Button(root,text = "20gr"))
        self.moneyButtons.append(tk.Button(root,text = "50gr"))
        self.moneyButtons.append(tk.Button(root,text = "1zl"))
        self.moneyButtons.append(tk.Button(root,text = "2zl"))
        self.moneyButtons.append(tk.Button(root,text = "5zl"))


        for i in self.moneyButtons:
            i.pack()
        self.canvas.pack()



root = tk.Tk()
app = Application(master=root)
app.mainloop()
print(0.1+0.2==0.3)