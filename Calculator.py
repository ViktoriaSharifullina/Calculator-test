import math
from tkinter import *
from decimal import *

mk = Tk()
mk.title('Calculator')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

activeStr = ''
stack = []


def division(x, y):
    check = 0.00000001
    try:
        result = x / y
        if y < check:
            raise ArithmeticError
        else:
            return result
    except ZeroDivisionError:
        raise ZeroDivisionError('Division by zero!')
    except ArithmeticError:
        raise ArithmeticError('Divisor less than 10^(-8)!!')


def addition(x, y):
    return x + y


def difference(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = addition(operand1, operand2)
    if operation == '-':
        result = difference(operand1, operand2)
    if operation == '/':
        result = division(operand1, operand2)
    if operation == '*':
        result = multiplication(operand1, operand2)
    label.configure(text=str(result))


def click(text):
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
    elif text == '.':
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            stack.clear()
            stack.append(label['text'])
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                stack.append(label['text'])  # добавляем цифру
                stack.append(text)  # добавляем знак
                activeStr = ''
                label.configure(text=text)
    return text


label = Label(mk, text='0', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")


def button_press(bt):
    # print("Button press: ", bt)
    return True


def buttonClick(event):
    b = event.widget  # use event info
    print(b['text'])  # cget text


button = [Button(mk, text='CE', command=lambda text='CE': (click(text), button_press(text)))]
# button[0].bind('<Button-1>', lambda e: buttonClick(e))
button[0].grid(row=1, column=3, sticky="nsew")

i = 1
for row in range(4):
    for col in range(4):
        button.append(Button(mk, text=buttons[row][col],
                             command=lambda row_=row, col_=col: (
                                 click(buttons[row_][col_]), button_press(buttons[row_][col_]))))
        button[i].grid(row=row + 2, column=col, sticky="nsew")
        # button[i].bind('<Button-1>', lambda e: buttonClick(e))
        i += 1

# button.bind('<Button-1>', lambda e: buttonClick(e))

mk.grid_rowconfigure(6, weight=1)
mk.grid_columnconfigure(4, weight=1)
# mk.mainloop()
