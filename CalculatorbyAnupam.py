from tkinter import *
win = Tk()
win.title("Calcualtor")
def btn_click(item):
    
    global expression

    expression = expression + str(item)

    input_text.set(expression)
    
def btn_clear():
    
    global expression

    expression = ""

    input_text.set("")
    
    
def btn_equal():
    
    global expression

    result = str(eval(expression)) 
    input_text.set(result)
    
    expression = "" 

expression = ""

input_text = StringVar()


e = Entry(win, textvariable = input_text, width = 50,borderwidth=5, bg= "cadet blue")
e.grid(row = 0, column = 0)
e.pack(ipady = 10)


butframe = Frame(win, width = 312, height = 272.5, bg = "gray")
butframe.pack()


but1= Button(butframe, text = "1",  width = 10, height = 3,bg="gray20", fg="white", command = lambda: btn_click(1))
but1.grid(row = 2, column = 0, padx = 1, pady = 1)
but2= Button(butframe, text = "2",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(2))
but2.grid(row = 2, column = 1, padx = 1, pady = 1)
but3= Button(butframe, text = "3",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(3))
but3.grid(row = 2, column = 2, padx = 1, pady = 1)
but4= Button(butframe, text = "4",  width = 10, height = 3,bg="gray20", fg="white",command = lambda: btn_click(4))
but4.grid(row = 1, column = 0, padx = 1, pady = 1)
but5 = Button(butframe, text = "5",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(5))
but5.grid(row = 1, column = 1, padx = 1, pady = 1)
but6= Button(butframe, text = "6",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(6))
but6.grid(row = 1, column = 2, padx = 1, pady = 1)
but7= Button(butframe, text = "7",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(7))
but7.grid(row = 0, column = 0, padx = 1, pady = 1)
but8 = Button(butframe, text = "8",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(8))
but8.grid(row = 0, column = 1, padx = 1, pady = 1)
but9= Button(butframe, text = "9",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(9))
but9.grid(row = 0, column = 2, padx = 1, pady = 1)
but0 = Button(butframe, text = "0",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click(0))
but0.grid(row = 3, column = 0, padx = 1, pady = 1)
dec= Button(butframe, text = ".",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click("."))
dec.grid(row = 3, column = 1, padx = 1, pady = 1)


add = Button(butframe, text = "+",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click("+"))
add.grid(row = 3, column = 2, padx = 1, pady = 1)
sub = Button(butframe, text = "-",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click("-"))
sub.grid(row = 3, column = 3, padx = 1, pady = 1)
cls= Button(butframe, text = "C",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_clear())
cls.grid(row = 0, column = 3, padx = 1, pady = 1)
div = Button(butframe, text = "/",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click("/"))
div.grid(row = 1, column = 3, padx = 1, pady = 1)
mul= Button(butframe, text = "*",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_click("*"))
mul.grid(row = 2, column = 3, padx = 1, pady = 1)
eql= Button(butframe, text = "=",  width = 10, height = 3,bg="gray20",fg="white", command = lambda: btn_equal())
eql.grid(row = 4, column = 3, padx = 1, pady=1)

a= Label(butframe, text ="CALCULATOR",bg= "gray", font=("Times", 24, "bold")).grid(row = 4, column =0, columnspan=3)



win.mainloop()
