import tkinter as tk
from tkinter import messagebox


def add_didjet(didjet):
    value = answer.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    answer.delete(0, tk.END)
    answer.insert(0, value+didjet)

def add_operation(operation):
    value = answer.get()
    if value[-1] in '-+*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*'in value or ':'in value:
        calculate()
        value = answer.get()
    answer.delete(0, tk.END)
    answer.insert(0, value+operation)

def calculate():
    value = answer.get()
    if value[-1] in '+-/*':
        operation = value[-1]
        value = value+value[:-1]
    answer.delete(0, tk.END)

    try:
        answer.insert(0, eval(value))
    except (NameError , SyntaxError):
        messagebox.showinfo('Внимание', 'Вы ввели недопустимые символы.')
        answer.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
        answer.insert(0, 0)

def cleare():
    answer.delete(0, tk.END)
    answer.insert(0, 0)

def make_button(didjet):
    return tk.Button(window, text=didjet, bd=5, font=('Arial', 13), command=lambda: add_didjet(didjet))


def make_operation(operation):
    return tk.Button(window, text=operation, bd=5, font=('Arial', 13),fg = 'blue',
                     command=lambda: add_operation(operation))
def make_ravno(operation):
    return tk.Button(window, text=operation, bd=5, font=('Arial', 13), fg='blue',
                     command=lambda: calculate())
def make_clear (operation):
    return tk.Button(window, text=operation, bd=5, font=('Arial', 13), fg='blue',
                     command=lambda: cleare())
def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_didjet(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
window = tk.Tk()
window.geometry(f"250x280+700+200")
window.config(bg='#FF0000')
window.title('Калькулятор')
window.bind('<Key>', press_key)

answer = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 15), width=15)
answer.insert(0, '0')
answer.grid(row=0, column=0, columnspan=4, stick='ew', padx=5, pady=5)
make_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)
make_ravno('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)


window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)
window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)

window.mainloop()
