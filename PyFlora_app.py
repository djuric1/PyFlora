from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("PyFloraPosuda")

myLabel1 = Label(root, text="User name")
myLabel2 = Label(root, text="Password")

myLabel1.grid(row=5, column=5)
myLabel2.grid(row=8, column=5)

# ent = Entry(root)
# ent.pack()

# def myClick():
#     myLabel = Label(root, text="You actually clicked it :O!")
#     myLabel.pack()


# myButton = Button(root, text="PRIJAVI ME")
# myButton.grid()
# myButton.pack()


root.mainloop()
