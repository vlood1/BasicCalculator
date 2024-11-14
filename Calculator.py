import tkinter



## Gets no1
def getno1():
    num1 = text_no1.get()
    num1 = int(num1)
    return(num1)

## Gets no2
def getno2():
    num2 = text_no2.get()
    num2 = int(num2)
    return(num2)


#Function that does the addition
def add():
    num1 = getno1()
    num2 = getno2()
    result = num1 + num2
    setresults(result, "+")
    
#A function that performs the subtraction
def sub():
    num1 = getno1()
    num2 = getno2()
    result = num1 - num2
    setresults(result, "-")

## Clear button
def clear():
    text_no1.delete(0, "end")
    text_no2.delete(0, "end")
    text_answer.delete(0, "end")

## Division function ÷
def div():
    num1 = getno1()
    num2 = getno2()
    result = num1 / num2
    setresults(result, "÷")

## Multiplication function x
def mlt():
    num1 = getno1()
    num2 = getno2()
    result = num1 * num2
    setresults(result, "x")

## Results
def setresults(result, sign):
    text_answer.delete(0, "end")
    num1 = getno1()
    num2 = getno2()
    text_answer.insert(0, f"{num1} {sign} {num2} = {result}")
    
    
    




# Way we made the gui (title and width)    
window = tkinter.Tk()
window.title("My Calculator")
window.geometry("300x300")
window.configure(background = "Silver")


#Labels

labelnum1 = tkinter.Label(window,text = "Enter the 1st number")
labelnum1.place(x = 2,y = 40)

labelnum2 = tkinter.Label(window,text = "Enter the 2nd number")
labelnum2.place(x = 2,y = 70)

labelresult = tkinter.Label(window,text = "Result >")
labelresult.place(x = 95,y = 250)

## Button section
button_add = tkinter.Button(window, text = "+", command = add,width = 4, height = 2, bg = "green", fg = "white")
button_add.place(x = 110,y = 110)

button_subtract = tkinter.Button(window, text = "-", command = sub,width = 4, height = 2, bg = "red", fg = "white")
button_subtract.place(x = 160,y = 110)

button_clear = tkinter.Button(window, text = "Clear", command = clear,width = 9, height = 2)
button_clear.place(x = 210, y = 42) 

button_division = tkinter.Button(window, text = "÷", command = div, width = 4, height = 2, bg = "blue", fg = "white")
button_division.place(x = 110,y = 160)

button_multiply = tkinter.Button(window, text = "x", command = mlt, width = 4, height = 2, bg = "MediumPurple", fg = "white")
button_multiply.place(x = 160,y = 160)

text_no1 = tkinter.Entry(window, width = 10)
text_no1.place(x = 125,y = 40)
text_no2 = tkinter.Entry(window, width = 10)
text_no2.place(x = 125, y = 70)
text_answer = tkinter.Entry(window, width = 20)
text_answer.place(x = 150, y = 250)


window.mainloop()
