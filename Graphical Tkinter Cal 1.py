#developed by Hosein Mohamadpor
from tkinter import *   #importing tkinter module

fvalue = ""


def click(event):       #defining applicable function
    global fvalue
    text = event.widget.cget("text")

    if text == "=":
        """when = is pressed the expression will be evaluated """
        if fvalue.get().isdigit():
            value = int(fvalue.get())
        else:
            try:
                value = eval(input_field.get())
            except Exception as e:
                print(e)
                value = "Error"

        fvalue.set(value)
        input_field.update()

    elif text == "clear":
        """when clear is pressed the input field will be reset """
        fvalue.set("")
        input_field.update()
    else:
        fvalue.set(fvalue.get() + text)
        input_field.update()

#__main__
        
root = Tk()
fvalue = StringVar()
fvalue.set("")
root.title("calculator developed by SOMDEV BEHERA")
input_field = Entry(root,textvar=fvalue, width=20, borderwidth=5)
input_field.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

#__creating buttons__

button1 = Button(root, text="1", padx=40, pady=20)
button2 = Button(root, text="2", padx=40, pady=20)
button3 = Button(root, text="3", padx=40, pady=20)
button4 = Button(root, text="4", padx=40, pady=20)
button5 = Button(root, text="5", padx=40, pady=20)
button6 = Button(root, text="6", padx=40, pady=20)
button7 = Button(root, text="7", padx=40, pady=20)
button8 = Button(root, text="8", padx=40, pady=20)
button9 = Button(root, text="9", padx=40, pady=20)
button0 = Button(root, text="0", padx=40, pady=20)
buttonplus = Button(root, text="+", padx=40, pady=20)
buttonminus = Button(root, text="-", padx=40, pady=20)
buttoninto = Button(root, text="*", padx=40, pady=20)
buttondivide = Button(root, text="/", padx=40, pady=20)
buttonequal = Button(root, text="=", padx=40, pady=20)
buttonclear = Button(root, text="clear", padx=40, pady=20)
buttonpoint=Button(root,text=".",padx=40,pady=20)
button_two_zero=Button(root,text="00",padx=40,pady=20)

#__binding buttons__

button1.grid(row=1, column=0)
button1.bind("<Button-1>", click)
button2.grid(row=1, column=1)
button2.bind("<Button-1>", click)
button3.grid(row=1, column=2)
button3.bind("<Button-1>", click)

button4.grid(row=2, column=0)
button4.bind("<Button-1>", click)
button5.grid(row=2, column=1)
button5.bind("<Button-1>", click)
button6.grid(row=2, column=2)
button6.bind("<Button-1>", click)

button7.grid(row=3, column=0)
button7.bind("<Button-1>", click)
button8.grid(row=3, column=1)
button8.bind("<Button-1>", click)
button9.grid(row=3, column=2)
button9.bind("<Button-1>", click)

button0.grid(row=0, column=0)
button0.bind("<Button-1>", click)

buttonplus.grid(row=0, column=4)
buttonplus.bind("<Button-1>", click)
buttonminus.grid(row=1, column=4)
buttonminus.bind("<Button-1>", click)
buttoninto.grid(row=2, column=4)
buttoninto.bind("<Button-1>", click)
buttondivide.grid(row=3, column=4)
buttondivide.bind("<Button-1>", click)
button_two_zero.grid(row=4,column=4)
button_two_zero.bind("<Button-1>",click)

buttonequal.grid(row=4, column=0)
buttonequal.bind("<Button-1>", click)
buttonclear.grid(row=4, column=1)
buttonclear.bind("<Button-1>", click)
buttonpoint.grid(row=4,column=2)
buttonpoint.bind("<Button-1>",click)


#__running mainloop__

root.mainloop()