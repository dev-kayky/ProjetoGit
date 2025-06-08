import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

TAXAS = {
    "BRL": {"USD": 0.19, "EUR": 0.17},
    "USD": {"BRL": 5.25, "EUR": 0.93},
    "EUR": {"BRL": 5.65, "USD": 1.07}
}

def converter():
    moeda_inicial = combo.inicial.get()
    moeda_final = combo.final.get()
    valor_str = entrada_valor.get()

    if not valor_str:
        messagebox.showerror("Erro!", "Digite um valor.")
        return

janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.configure(bg="black")
label_inicial = tk.Label(janela, text="Conversor de Moedas - Início", fg="white", bg="black")
label_inicial.pack(padx=20, pady=20)
moedas = list(TAXAS.keys())
moeda_inicial_var = tk.StringVar(janela)
moeda_final_var = tk.StringVar(janela)
valor_entrada = tk.Entry(janela)
resultado = tk.StringVar(janela)

janela.mainloop()