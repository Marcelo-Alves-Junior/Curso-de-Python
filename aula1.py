# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Importar a base de dados do Produto 
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir cadastro para todos os produtos

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2: Fazer Login
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=768, y=371)
pyautogui.write("teste@teste.com")
pyautogui.press("tab")
pyautogui.write("teste_senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de dados do Produto
tabela = pandas.read_csv("C:/Users/Dev/Desktop/Projetos Pessoais/Python Hashtag/Curso-de-Python/produtos.csv")
print(tabela) 

# Passo 4: Cadastrar 1 produto
def cadastrar_produto (linha):
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

# Passo 5: Repetir cadastro para todos os produtos

for linha in tabela.index:
    pyautogui.click(x=880, y=257)
    cadastrar_produto(linha)
    pyautogui.scroll(1000)