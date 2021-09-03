from tkinter import *
from math import *


win = Tk()
win.config(bg = 'orange')
win.geometry('500x600')
win.resizable(0,0)
win.title('Calculator')


expression = ''


def click_button(number):
    global expression
    expression += str(number)
    input_text.set(expression)


def clear_everything():
    global expression
    expression = ''
    input_text.set('')


input_text = StringVar()
get_number_entry = Entry(win,textvariable = input_text,fg = 'white',bg = 'blue' ,width = 73)
get_number_entry.place(relx = 0.05, rely = 0.05)


def calculation():

    try:
        global expression
        total = str(eval(expression))

        input_text.set(total)
        expression = ''


    except:
        input_text.set('ERROR')
        expression = ''


def Delete_Last_Character():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


    

button1 = Button(win, text = '1', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(1))
button1.place(relx = 0.05, rely = 0.1)


button2 = Button(win, text = '2', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(2))
button2.place(relx = 0.20, rely = 0.1)


button3 = Button(win, text = '3', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(3))
button3.place(relx = 0.35, rely = 0.1)


button4 = Button(win, text = '4', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(4))
button4.place(relx = 0.05, rely = 0.19)


button5 = Button(win, text = '5', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(5))
button5.place(relx = 0.20, rely = 0.19)


button6 = Button(win, text = '6', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(6))
button6.place(relx = 0.35, rely = 0.19)


button7 = Button(win, text = '7', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(7))
button7.place(relx = 0.05, rely = 0.28)


button8 = Button(win, text = '8', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(8))
button8.place(relx = 0.20, rely = 0.28)


button9 = Button(win, text = '9', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(9))
button9.place(relx = 0.35, rely = 0.28)


button0 = Button(win, text = '0', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(0))
button0.place(relx = 0.20, rely = 0.37)


button00 = Button(win, text = '00', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('00'))
button00.place(relx = 0.35, rely = 0.37)


point_button = Button(win, text = '.', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('.'))
point_button.place(relx = 0.65, rely = 0.37)



divide_button = Button(win, text = '/', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('/'))
divide_button.place(relx = 0.50, rely = 0.1)


button000 = Button(win, text = '000', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                activebackground = 'purple',command = lambda : click_button('000'))
button000.place(relx = 0.05, rely = 0.37)


multiply_button = Button(win, text = '×', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('*'))
multiply_button.place(relx = 0.50, rely = 0.19)


plus_button = Button(win, text = '+', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('+'))
plus_button.place(relx = 0.50, rely = 0.28)


mines_button = Button(win, text = '-', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('-'))
mines_button.place(relx = 0.50, rely = 0.37)


CE_button = Button(win, text = 'CE', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = clear_everything)
CE_button.place(relx = 0.65, rely = 0.10)


power_button = Button(win, text = 'x^2', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('**'))
power_button.place(relx = 0.65, rely = 0.19)


sqrt_button = Button(win, text = '√x', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('sqrt'))
sqrt_button.place(relx = 0.65, rely = 0.28)


equal_button = Button(win, text = '=', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = calculation)
equal_button.place(relx = 0.80, rely = 0.37)

open_bracket_button = Button(win, text = '(', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button('('))
open_bracket_button.place(relx = 0.80, rely = 0.1)


close_bracket_button = Button(win, text = ')', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = lambda : click_button(')'))
close_bracket_button.place(relx = 0.80, rely = 0.19)


delete_last_character = Button(win, text = 'C', bg = 'blue',fg = 'white' ,width = 8, height = 2,
                 activebackground = 'purple',command = Delete_Last_Character)
delete_last_character.place(relx = 0.80, rely = 0.28)



win.mainloop()