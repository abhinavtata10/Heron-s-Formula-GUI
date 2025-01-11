from tkinter import *
from math import *

window=Tk()
window.title("Area formula GUI")
window.geometry("850x400")
window.configure(bg="tan",padx=10, pady=10)

def calculate_area():
    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())
    sp = (a + b + c) / 2
    area = sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    labelD.configure(text=f"The area is: {area} square units")


frameA = Frame(window, bg="red")
frameA.pack()
frameB = Frame(window, bg="red")
frameB.pack()
frameC = Frame(window, bg="red")
frameC.pack()
frameD = Frame(window, bg="red")
frameD.pack()
frameE = Frame(window, bg="red")
frameE.pack()

labelA = Label(frameA, text="a:", font=("Courier", 20), bg="blue", padx=5, pady=5)
labelB = Label(frameB, text="b:", font=("Courier", 20), bg="blue", padx=5, pady=5)
labelC = Label(frameC, text="c:", font=("Courier", 20), bg="blue", padx=5, pady=5)

labelA.pack(side=LEFT)
labelB.pack(side=LEFT)
labelC.pack(side=LEFT)

entryA = Entry(frameA, bg="white", fg="black")
entryB = Entry(frameB, bg="white", fg="black")
entryC = Entry(frameC, bg="white", fg="black")

entryA.pack(side=RIGHT)
entryB.pack(side=RIGHT)
entryC.pack(side=RIGHT)


button = Button(frameD, text="Calculate the Area", font=("Courier", 27), bg="blue", fg="Black", command=calculate_area)
button.pack()

labelD = Label(frameE, text="The area is: ____ square units", font=("Courier", 27), bg="blue")
labelD.pack()

window.mainloop()