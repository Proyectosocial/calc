
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Calculadora')
root.geometry('400x500')
root.resizable(0, 0)

color_texto = '#000000'
color_boton = '#e0e0e0'
color_boton_igual = '#4caf50'
color_boton_clear = '#f44336'

screen_text = tk.StringVar()
screen_label = tk.Label(root, textvariable=screen_text, font=('Arial', 30), bg='#ffffff', fg=color_texto,
anchor='e', padx=10)
screen_label.grid(row=0, column=0, columnspan=4, sticky='we', pady=10)

expresion = ''

def press(num):
    global expresion
    expresion += str(num)
    screen_text.set(expresion)

def equalpress():
    try:
        global expresion
        result = str(eval(expresion))
        screen_text.set(result)
        expresion = result
    except Exception as e:
        messagebox.showerror("Error", "Entrada no válida")
        screen_text.set('')
        expresion = ''

def clear():
    global expresion
    screen_text.set('')
    expresion = ''

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, font=('Arial', 18), bg=color_boton, fg=color_texto, command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

# Botón Igual
equal_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), bg=color_boton_igual, fg='#ffffff', command=equalpress)
equal_button.grid(row=4, column=3, padx=5, pady=5, sticky='nsew')

# Botón Limpiar
clear_button = tk.Button(root, text='Clear', width=5, height=2, font=('Arial', 18), bg=color_boton_clear, fg='#ffffff', command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

# Configuración de pesos para redimensionamiento
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
