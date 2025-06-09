import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

TAXAS = {
    "BRL": {"USD": 0.19, "EUR": 0.17},
    "USD": {"BRL": 5.25, "EUR": 0.93},
    "EUR": {"BRL": 5.65, "USD": 1.07}
}

def converter():
    moeda_inicial = combo_inicial.get()
    moeda_final = combo_final.get()
    valor_str = entrada_valor.get()

    if not valor_str:
        messagebox.showerror("Erro!", "Digite um valor.")
        return

janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.configure(bg="black")
label_inicial = tk.Label(janela, text="Conversor de Moedas - Início", fg="white", bg="black")
label_inicial.pack(padx=20, pady=20)
frame = ttk.Frame(janela)
frame.pack(padx=10, pady=10)
moedas = list(TAXAS.keys())
moeda_inicial_var = tk.StringVar(janela)
moeda_final_var = tk.StringVar(janela)
valor_entrada = tk.Entry(janela)
resultado = tk.StringVar(janela)
label_moeda1 = ttk.Label(frame, text="Moeda à ser convertida:")
label_moeda1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
combo_inicial = ttk.Combobox(frame, textvariable=moeda_inicial_var, values=moedas, width=10)
combo_inicial.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
combo_inicial.set("BRL")
label_moeda2 = ttk.Label(frame, text="Moeda para qual será convertida:")
label_moeda2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
combo_final = ttk.Combobox(frame, textvariable=moeda_final_var, values=moedas, width=10)
combo_final.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
combo_final.set("USD")
label_valor = ttk.Label(frame, text="Valor para a conversão:")
label_valor.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_valor = ttk.Entry(frame, width=15)
entrada_valor.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

janela.mainloop()