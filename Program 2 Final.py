from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Enter your Fullname:', fg="red")
        self.lbl1.place(x=20, y=50)
        self.t1 = Entry(bd=3)
        self.t1.place(x=200, y=50)
        self.b1 = Button(win, text='Click to display your Fullname', fg="red", command=self.click)
        self.b1.place(x=20, y=100)
        self.t3 = Entry(bd=3)
        self.t3.place(x=200, y=100)
    def click(self):
        result= str(self.t1.get())
        self.t3.insert(END, str(result))
window=Tk()
mywin=MyWindow(window)
window.title('Midterm in OOP')
window.geometry("400x300+10+10")
window.mainloop()