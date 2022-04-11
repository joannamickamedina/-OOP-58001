from tkinter import *
window = Tk()

window.geometry("400x150+10+20")
window.title("Major Subjects")

data = "reading", "writing", "arithmetic", "coding"
lb = Listbox(window, height=5, selectmode="single")
for num in data:
    lb.insert(END, num)
lb.place(x=130)

window.mainloop()