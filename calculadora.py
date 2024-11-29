import tkinter as tk
from tkinter import messagebox

def btn_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            messagebox.showerror("Erro", "Entrada inválida!")
            screen.set("")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Configurar o tamanho da janela
root.geometry("300x400")
root.resizable(0, 0)

# Variável para armazenar o texto da tela
screen = tk.StringVar()

# Tela da calculadora
entry = tk.Entry(root, textvar=screen, font="Arial 20", borderwidth=2, relief="ridge")
entry.pack(fill="x", ipadx=8, ipady=8, padx=10, pady=10)

# Criar os botões
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+"
]

row, col = 0, 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="Arial 15 bold", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", btn_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Iniciar o loop da interface
root.mainloop()
