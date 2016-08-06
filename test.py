from tkinter import *
import functions

window = Tk()

top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

display = Entry(top_row, width=45, bg="light green")
display.grid()

num_pad = Frame(window)
num_pad.grid(row=1, column = 0, sticky = W)
button1 = Button(num_pad, text="1", width=5).grid(row=0, column = 0)

operator = Frame(window)
operator.grid(row = 1, column = 1, sticky=E)
button_plus = Button(operator, text="+", width = 5).grid(row = 0, column = 0)

num_pad_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '=']
operator_list = ['*', '/', '+', '-', '(', ')', 'C']

def click(key):
    if key == '=':
        try:
            result = str(eval(display.get()))
        except:
            result = "--> 오류"
        display.delete(0, END)
        display.insert(END, result)

    elif key == 'C':
        display.delete(0, END)
    elif key == '+':
        display.insert(END, key)
    elif key == '-':
        display.insert(END, key)
    elif key == '/':
        display.insert(END, key)
    elif key == '*':
        display.insert(END, key)
    elif key == '(':
        display.insert(END, key)
    elif key == ')':
        display.insert(END, key)

    elif key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[1]:
        display.insert(END, "300000000")
    elif key == constants_list[2]:
        display.insert(END, "330")
    elif key == constants_list[3]:
        display.insert(END, "149597887.5")

    elif key == functions_list[0]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, functions.factorial(n))
    elif key == functions_list[1]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, functions.to_roman(n))
    elif key == functions_list[2]:
        n = display.get()
        display.delete(0, END)
        display.insert(END, functions.to_binary(n))
    elif key == functions_list[3]:
     n = display.get()
     display.delete(0, END)
     display.insert(END, functions.from_binary(n))

    else :
        display.insert(END, key)

r = 0; c = 0
for btn_text in operator_list:
    def cmd(x = btn_text):
        click(x)

    Button(operator, text = btn_text, width = 5, command = cmd) \
    .grid(row = r, column = c)

    c += 1
    if c > 2 :
        c = 0; r += 1

r = 0; c = 0
for btn_text in num_pad_list:
    def cmd(x = btn_text):
        click(x)

    Button(num_pad, text = btn_text, width = 5, command = cmd) \
        .grid(row = r, column = c)

    c += 1
    if c > 2:
        c = 0
        r += 1

# button_groups = {
#     'num':{'list':num_pad_list, 'window':num_pad, 'width':5, 'cols':3},
#     'op':{'list':operator_list, 'window':operator, 'width':5, 'cols':2},
# }

constants_list = ['pi', '빛의 이동 속도(m/s)', '소리의 이동속도(m/s', '태양과의 평균거리(km)']
functions_list = ['factorial(!)', '-> roman', '-> binary', 'binary->10']

# constants frame
constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)  # W = west

# functions frame
functions = Frame(window)
functions.grid(row=3, column=1, sticky=E)  # E = east

button_groups = {
    'consts': {'list': constants_list, 'window': constants, 'width': 22, 'cols': 1},
    'funcs': {'list': functions_list, 'window': functions, 'width': 13, 'cols': 1},
}

for label in button_groups.keys():

    r = 0;
    c = 0
    buttons = button_groups[label]
    for btn_text in buttons['list']:
        def cmd(x=btn_text):
            click(x)


        Button(buttons['window'],
               text=btn_text,
               width=buttons['width'],
               command=cmd).grid(row=r, column=c)
        c = c + 1
        if c >= buttons['cols']:
            c = 0
            r = r + 1