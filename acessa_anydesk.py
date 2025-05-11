import pandas as pd
import subprocess
import pyautogui
from time import sleep

def buscar_anydesk(nome_posto, numero_pdv):
    dados = pd.read_excel("") #Colocar o caminho da planilha a ser consultada.

    dados.columns = dados.columns.str.strip().str.upper()# Tirando os espaços no final e começo e deixando Tudo maiusculo.
    dados['NOME DO POSTO'] = dados['NOME DO POSTO'].str.strip().str.upper().str.replace(" ","") # Agora tirando os espços entre as palavras.

    nome_posto = nome_posto.strip().upper().replace(" ", "") # Pegando o valor recebido pelo usuario e Tirando espaços e Deixando tudo maiusculo.
    numero_pdv = "PDV" + numero_pdv.strip().upper().replace(" ","") # Pegando o valor recebido pelo usuario e Tirando espaços e Deixando tudo maiusculo.

    posto_dados = dados[dados['NOME DO POSTO'] == nome_posto] # Criando uma varialvel para consultar se o valor recebido tem na planilha.

    # Se o nome do Posto não estiver na planilha ele retorna um erro.
    if posto_dados.empty:
        messagebox.showerror(f'Posto {nome_posto} não encontrado.')
        return
    
    # Se o numero do PDV não estiver na planilha ele retorna um erro.
    if numero_pdv not in posto_dados.columns:
        messagebox.showerror(f"O PDV {numero_pdv} não possui AnyDesk registrado.")
        return
    
    valor = posto_dados.iloc[0][numero_pdv]
    # Se o valor inserido pelo usuario não for válido ele retorna um erro.
    if pd.isna(valor):
        messagebox.showerror(f"O número do PDV {numero_pdv} é inválido.")
        return
    
    try:
        # Pega o número do Anydesk do PDV e coloca nessa váriavel tirando os espaços.
        anydesk = int(str(valor).replace(" ", ""))
        # Abri o Anydesk e coloca o número do anydesk do PDV que você deseja acessar.
        comando = f'"C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe" {anydesk}'
        subprocess.Popen(comando, shell=True)

        sleep(8) # Aguarda 8 segundos para dar tempo de abrir a janela da senha.

        pyautogui.write('') # Coloca a senha para acessar.
        pyautogui.press('enter') # Pressiona a tecla enter para confirmar a senha.

    except Exception as e:
        # Caso de algo errado, retorna esse erro.
        messagebox.showerror("Erro ao tentar abrir o AnyDesk: ", e)

# Função de ação após o botão "Acessar o Posto" ser acionado.
def botao():
    nome_posto = entry_posto.get() # Uma variavel que recebe o nome do posto que o usuario colocou.
    numero_pdv = entry_pdv.get() # Uma variavel que recebe o número do PDV que o usuario colocou.
    buscar_anydesk(nome_posto, numero_pdv) # Chama a função buscar_anydesk passando os valores resgatados.

# ==== INTERFACE TKINTER ====

import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()
janela.title("Buscar Anydesk")
janela.geometry("500x250")

centralizar = tk.Frame(janela)
centralizar.place(relx=0.5, rely=0.5, anchor='center')

posto = tk.Label(centralizar, text="Qual Posto você quer acessar")
posto.grid(row=0, column=0, padx=10, pady=10, sticky='e')

entry_posto = tk.Entry(centralizar, width=20)
entry_posto.grid(row=0, column=1, padx=10, pady=10)

pdv = tk.Label(centralizar, text="Qual PDV você quer acessar")
pdv.grid(row=1, column=0, padx=10, pady=10, sticky='e')

entry_pdv = tk.Entry(centralizar, width=20)
entry_pdv.grid(row=1, column=1, padx=10, pady=10)

btn_acessar = tk.Button(centralizar, text="Acessar o Posto", command=botao)
btn_acessar.grid(row=2,column=0, columnspan=2, pady=20)

janela.mainloop()