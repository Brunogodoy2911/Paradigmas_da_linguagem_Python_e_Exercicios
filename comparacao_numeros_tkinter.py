# Crie um programa com interface gráfica em Python que receba dois números, compare-os e informe se o primeiro é maior, menor ou igual ao segundo.

import tkinter as tk
from tkinter import messagebox

def compara_numeros():
  try:
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
  
    if num1 > num2:
      messagebox.showinfo("Resultado da comparação", f"O Número 1: {num1} é maior que Número 2: {num2}")
    elif num2 > num1:
      messagebox.showinfo("Resultado da comparação", f"O Número 1: {num1} é menor que Número 2: {num2}")
    else:
      messagebox.showinfo("Resultado da comparação", f"O Número 1: {num1} é igual ao Número 2: {num2}")
  except ValueError:
      messagebox.showerror("Erro de Entrada", "Por favor, digite apenas números válidos.")


janela = tk.Tk()
janela.title("Comparador de Número")


label_num1 = tk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_num1 = tk.Entry(janela)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_num2 = tk.Entry(janela)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

botao_comparar = tk.Button(janela, text="Comparar Números", command=compara_numeros)
botao_comparar.grid(row=2, columnspan=2, padx=10, pady=5)

janela.mainloop()