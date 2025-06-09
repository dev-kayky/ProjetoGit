import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

TAXAS = {
    "BRL": {
        "USD": 0.19, "EUR": 0.17, "GBP": 0.15, "JPY": 29.00,
        "CAD": 0.26, "AUD": 0.29, "CHF": 0.17
    },
    "USD": {
        "BRL": 5.25, "EUR": 0.93, "GBP": 0.81, "JPY": 155.00,
        "CAD": 1.37, "AUD": 1.50, "CHF": 0.90
    },
    "EUR": {
        "BRL": 5.65, "USD": 1.07, "GBP": 0.88, "JPY": 165.00,
        "CAD": 1.48, "AUD": 1.62, "CHF": 0.97
    },
    "GBP": {
        "BRL": 6.55, "USD": 1.23, "EUR": 1.14, "JPY": 190.00,
        "CAD": 1.70, "AUD": 1.85, "CHF": 1.11
    },
    "JPY": {
        "BRL": 0.034, "USD": 0.0064, "EUR": 0.0061, "GBP": 0.0053,
        "CAD": 0.0088, "AUD": 0.0097, "CHF": 0.0058
    },
    "AUD": {
        "BRL": 3.45, "USD": 0.67, "EUR": 0.61, "GBP": 0.54,
        "JPY": 103.00, "CAD": 0.92, "CHF": 0.61
    },
    "CAD": {
        "BRL": 3.85, "USD": 0.73, "EUR": 0.67, "GBP": 0.59,
        "JPY": 113.00, "AUD": 1.09, "CHF": 0.70
    },
    "CHF": {
        "BRL": 5.80, "USD": 1.11, "EUR": 1.03, "GBP": 0.90,
        "JPY": 172.00, "CAD": 1.42, "AUD": 1.63
    }
}

def converter():
    moeda_inicial = combo_inicial.get()
    moeda_final = combo_final.get()
    valor_str = entrada_valor.get()

    if not valor_str:
        messagebox.showerror("Erro!", "Digite um valor.")
        return
    try:
        valor = float(valor_str)
        if valor < 0:
            messagebox.showerror("Erro!", "O valor não pode ser negativo.")
            return
    except ValueError:
        messagebox.showerror("Erro!", "Entrada inválida. Digite um número.")
        return
    
    if moeda_inicial == moeda_final:
        resultado.set(f"{valor:.2f} {moeda_inicial}")
        return
    
    if moeda_inicial in TAXAS and moeda_final in TAXAS and moeda_final in TAXAS.get(moeda_inicial, {}):
        taxa = TAXAS.get(moeda_inicial, {}).get(moeda_final)
        valor_convertido = valor * taxa
        resultado.set(f"{valor_convertido:.2f} {moeda_final}")
    else:
        messagebox.showerror("Erro!", "Não foi possível converter.")

def limpar():
    entrada_valor.delete(0, tk.END)
    resultado.set("")

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
botoes = tk.Frame(janela, bg="black")
botoes.pack(pady=10)
tk.Button(botoes, text="Converter", command=converter, bg="white", fg="black").grid(row=0, column=0, padx=10)
tk.Button(botoes, text="Limpar", command=limpar, bg="white", fg="black").grid(row=0, column=1, padx=10)
resultado = tk.StringVar()
tk.Label(janela, text="Resultado:", font=("Segoe UI", 11, "bold"), fg="white", bg="black").pack(pady=(10, 0))
label_resultado = tk.Label(janela, textvariable=resultado, font=("Segoe UI", 12), fg="white", bg="gray20", padx=10, pady=5)
label_resultado.pack(pady=5, padx=20, fill="x")

janela.mainloop()