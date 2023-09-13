from tkinter import *

expression = ""

def insert_text(number):
	global expression
	expression = expression + str(number)

	equation.set(expression)


def evaluate():
	try:

		global expression
		
		total = str(eval(expression))

		equation.set(total)

		expression = ""
		
	except:

		equation.set("ERROR")
		expression = ""

def clear():
	global expression
	equation.set("")
	expression = ""


window = Tk()
window.title("Calculator")
window.geometry("300x450")

equation = StringVar()

field = Entry(window, textvariable=equation)

field.grid(columnspan=4, ipadx=70)

button1 = Button(window, text='1', fg='black',command=lambda: insert_text(1), height=1, width=7)
button1.grid(row=2, column=0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button2 = Button(window, text='2', fg='black',command=lambda: insert_text(2), height=1, width=7)
button2.grid(row=2, column=1, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button3 = Button(window, text='3', fg='black',command=lambda: insert_text(3), height=1, width=7)
button3.grid(row=2, column=2, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button4 = Button(window, text='4', fg='black',command=lambda: insert_text(4), height=1, width=7)
button4.grid(row=3, column=0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button5 = Button(window, text='5', fg='black',command=lambda: insert_text(5), height=1, width=7)
button5.grid(row=3, column=1, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button6 = Button(window, text='6', fg='black',command=lambda: insert_text(6), height=1, width=7)
button6.grid(row=3, column=2, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button7 = Button(window, text='7', fg='black',command=lambda: insert_text(7), height=1, width=7)
button7.grid(row=4, column=0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button8 = Button(window, text='8', fg='black',command=lambda: insert_text(8), height=1, width=7)
button8.grid(row=4, column=1, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button9 = Button(window, text='9', fg='black',command=lambda: insert_text(9), height=1, width=7)
button9.grid(row=4, column=2, padx = 10, pady = 10, ipadx = 10, ipady = 10)

button0 = Button(window, text='0', fg='black',command=lambda: insert_text(0), height=1, width=7)
button0.grid(row=5, column=0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

decimal = Button(window, text='.', fg='black',command=lambda: insert_text('.'), height=1, width=7)
decimal.grid(row=5, column=1, padx = 10, pady = 10, ipadx = 10, ipady = 10)

clear = Button(window, text='Clear', fg='black',command=clear, height=1, width=7)
clear.grid(row=5, column='2', padx = 10, pady = 10, ipadx = 10, ipady = 10)

plus = Button(window, text='+', fg='black',command=lambda: insert_text("+"), height=1, width=7)
plus.grid(row=6, column=0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

minus = Button(window, text='-', fg='black',command=lambda: insert_text("-"), height=1, width=7)
minus.grid(row=6, column=1, padx = 10, pady = 10, ipadx = 10, ipady = 10)

multiply = Button(window, text='*', fg='black',command=lambda: insert_text("*"), height=1, width=7)
multiply.grid(row=6, column=2, padx = 10, pady = 10, ipadx = 10, ipady = 10)

divide = Button(window, text='/', fg='black',command=lambda: insert_text("/"), height=1, width=7)
divide.grid(row=7, column=0, padx = 10, pady = 10, ipadx = 10, ipady = 10)

equal = Button(window, text='=', fg='black',command=evaluate, height=1, width=7)
equal.grid(row=7, column=1, padx = 10, pady = 10, ipadx = 10, ipady = 10)



window.mainloop()