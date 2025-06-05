import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# taxas de conversão entre moedas
TAXAS = {
    "BRL": {"USD": 0.19, "EUR": 0.17},
    "USD": {"BRL": 5.25, "EUR": 0.93},
    "EUR": {"BRL": 5.65, "USD": 1.07}
}

janela = tk.Tk()
janela.title("Conversor de Moedas - Inicial")

label_inicial = ttk.Label(janela, text="Configuração inicial do conversor.")
label_inicial.pack(padx=20, pady=20)

janela.mainloop()