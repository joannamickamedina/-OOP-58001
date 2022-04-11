from tkinter import *
window=Tk()

label = Label(window, text='Enter your fullname: ', fg='red')
label.place(x=20, y=50)

txtfld = Entry(window, text="This is a text field", bd=5)
txtfld.place(x=200, y=50)

button = Button(window, text='Click to display you Fullname', fg='red')
button.place(x=20, y=100)

txtfld = Entry(window, text="This is a text field", bd=5)
txtfld.place(x=200, y=100)


window.title('Midterm in OOP')
window.geometry("400x200+10+10")
window.mainloop()
