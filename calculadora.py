import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Entrada de texto
entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: on_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botón de limpiar
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row_val, column=col_val)

# Ejecutar la aplicación
root.mainloop()
