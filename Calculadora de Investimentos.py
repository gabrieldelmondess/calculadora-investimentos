import tkinter as tk
from tkinter import messagebox

def calcular_fgts_com_aportes(saldo_inicial, deposito_mensal, juros_ano=0.056, meses=12):
    """
    Calcula o saldo futuro do FGTS considerando depósitos mensais e juros compostos anuais.
    """
    juros_mensal = (1 + juros_ano)**(1/12) - 1
    saldo_futuro = saldo_inicial * (1 + juros_mensal)**meses
    
    if juros_mensal > 0:
        saldo_futuro += calcular_valor_futuro_depositos_regulares(deposito_mensal, juros_mensal, meses)
    else:
        saldo_futuro += deposito_mensal * meses
    
    return saldo_futuro

def calcular_valor_futuro_depositos_regulares(deposito_mensal2, taxa_juros_mensal, numero_meses):
    """
    Calcula o valor futuro de depósitos regulares aplicados com juros compostos.
    """
    if taxa_juros_mensal == 0:
        return deposito_mensal2 * numero_meses
    else:
        fator_juros = (1 + taxa_juros_mensal)
        valor_futuro = fator_juros * (((fator_juros**numero_meses) - 1) / taxa_juros_mensal) * deposito_mensal2
        return valor_futuro

# Função para calcular o FGTS
def calcular_fgts():
    try:
        saldo_inicial = float(entry_saldo_inicial.get())
        deposito_mensal = float(entry_deposito_mensal.get())
        juros_ano = float(entry_juros_ano.get()) / 100  # Converter para decimal
        meses = int(entry_meses.get())
        
        resultado = calcular_fgts_com_aportes(saldo_inicial, deposito_mensal, juros_ano, meses)
        
        label_resultado.config(text=f"Saldo do FGTS após {meses} meses: R${resultado:.2f}")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")

# Função para calcular o valor futuro de depósitos regulares
def calcular_depositos_regulares():
    try:
        # Pegando os valores dos campos de entrada
        deposito_mensal = float(entry_deposito_mensal2.get())  # Verifique se é o entry correto
        juros_ano = float(entry_juros_ano2.get()) / 100  # Convertendo de percentual para decimal
        meses = int(entry_meses2.get())  # Número de meses de aporte
        
        # Convertendo juros anual para mensal
        taxa_juros_mensal = (1 + juros_ano)**(1/12) - 1
        
        # Calculando o valor futuro dos depósitos regulares
        resultado = calcular_valor_futuro_depositos_regulares(deposito_mensal, taxa_juros_mensal, meses)
        
        # Atualizando o resultado na interface
        label_resultado2.config(text=f"Valor futuro dos depósitos após {meses} meses: R${resultado:.2f}")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos!")


# Função para mostrar a tela de cálculo do FGTS
def mostrar_tela_fgts():
    frame_tela_inicial.grid_forget()
    frame_fgts.grid(row=0, column=0)

# Função para mostrar a tela de cálculo dos depósitos regulares
def mostrar_tela_depositos():
    frame_tela_inicial.grid_forget()
    frame_depositos.grid(row=0, column=0)

# Função para voltar para a tela inicial
def voltar_para_tela_inicial():
    frame_fgts.grid_forget()
    frame_depositos.grid_forget()
    frame_tela_inicial.grid(row=0, column=0)

# Criando a janela principal
root = tk.Tk()
root.title("Cálculo de Finanças e Investimentos")

# Tela Inicial
frame_tela_inicial = tk.Frame(root)
frame_tela_inicial.grid(row=0, column=0, padx=10, pady=10)

label_tela_inicial = tk.Label(frame_tela_inicial, text="Escolha o Cálculo:")
label_tela_inicial.grid(row=0, column=0, padx=10, pady=10)

botao_fgts = tk.Button(frame_tela_inicial, text="Cálculo FGTS", command=mostrar_tela_fgts)
botao_fgts.grid(row=1, column=0, padx=10, pady=10)

botao_depositos = tk.Button(frame_tela_inicial, text="Valor Futuro Depósitos Regulares", command=mostrar_tela_depositos)
botao_depositos.grid(row=2, column=0, padx=10, pady=10)

# Tela de Cálculo de FGTS
frame_fgts = tk.Frame(root)

label_saldo_inicial = tk.Label(frame_fgts, text="Saldo Inicial (R$):")
label_saldo_inicial.grid(row=0, column=0, padx=10, pady=10)
entry_saldo_inicial = tk.Entry(frame_fgts)
entry_saldo_inicial.grid(row=0, column=1, padx=10, pady=10)

label_deposito_mensal = tk.Label(frame_fgts, text="Depósito Mensal (R$):")
label_deposito_mensal.grid(row=1, column=0, padx=10, pady=10)
entry_deposito_mensal = tk.Entry(frame_fgts)
entry_deposito_mensal.grid(row=1, column=1, padx=10, pady=10)

label_juros_ano = tk.Label(frame_fgts, text="Taxa de Juros Anual (%):")
label_juros_ano.grid(row=2, column=0, padx=10, pady=10)
entry_juros_ano = tk.Entry(frame_fgts)
entry_juros_ano.grid(row=2, column=1, padx=10, pady=10)

label_meses = tk.Label(frame_fgts, text="Período (Meses):")
label_meses.grid(row=3, column=0, padx=10, pady=10)
entry_meses = tk.Entry(frame_fgts)
entry_meses.grid(row=3, column=1, padx=10, pady=10)

botao_calcular_fgts = tk.Button(frame_fgts, text="Calcular FGTS", command=calcular_fgts)
botao_calcular_fgts.grid(row=4, column=0, columnspan=2, pady=20)

label_resultado = tk.Label(frame_fgts, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2, pady=10)

botao_voltar = tk.Button(frame_fgts, text="Voltar", command=voltar_para_tela_inicial)
botao_voltar.grid(row=6, column=0, columnspan=2, pady=10)

# Tela de Cálculo de Depósitos Regulares
frame_depositos = tk.Frame(root)

label_deposito_mensal2 = tk.Label(frame_depositos, text="Depósito Mensal (R$):")
label_deposito_mensal2.grid(row=0, column=0, padx=10, pady=10)
entry_deposito_mensal2 = tk.Entry(frame_depositos)
entry_deposito_mensal2.grid(row=0, column=1, padx=10, pady=10)

label_juros_ano2 = tk.Label(frame_depositos, text="Taxa de Juros Anual (%):")
label_juros_ano2.grid(row=1, column=0, padx=10, pady=10)
entry_juros_ano2 = tk.Entry(frame_depositos)
entry_juros_ano2.grid(row=1, column=1, padx=10, pady=10)

label_meses2 = tk.Label(frame_depositos, text="Período (Meses):")
label_meses2.grid(row=2, column=0, padx=10, pady=10)
entry_meses2 = tk.Entry(frame_depositos)
entry_meses2.grid(row=2, column=1, padx=10, pady=10)

botao_calcular_depositos = tk.Button(frame_depositos, text="Calcular Depósitos", command=calcular_depositos_regulares)
botao_calcular_depositos.grid(row=3, column=0, columnspan=2, pady=20)

label_resultado2 = tk.Label(frame_depositos, text="Resultado:")
label_resultado2.grid(row=4, column=0, columnspan=2, pady=10)

botao_voltar2 = tk.Button(frame_depositos, text="Voltar", command=voltar_para_tela_inicial)
botao_voltar2.grid(row=5, column=0, columnspan=2, pady=10)

# Exibindo a tela inicial
root.mainloop()
