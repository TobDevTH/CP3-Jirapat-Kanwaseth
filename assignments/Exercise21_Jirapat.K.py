from tkinter import *
import math

def leftClickButton(event):
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    print(result)

    if(result < 18.5):
        labelResult.configure(text="ผอมเกินไป")
    elif(result <23.0):
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif (result < 25.0):
        labelResult.configure(text="น้ำหนักเกิน")
    elif (result < 30.0):
        labelResult.configure(text="อ้วน")
    elif (result >= 30.0):
        labelResult.configure(text="อ้วนมาก")
    else:
        labelResult.configure(text="Error!!")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()