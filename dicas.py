#Dicas para automatizar

# Biblioteca para aguardar carregamento da tela
import time

time.sleep(3)

# Biblioteca para pegar posição do mouse (Utilizar o time.sleep para posicionar o mouse aonde se quer pegar a posição)
# Demais funções acessar: https://pyautogui.readthedocs.io/en/latest/index.html
import pyautogui

print(pyautogui.position())

# Biblioteca para importar arquivos excel, csv e etc

import pandas

tabela = pandas.read_csv("C:/Users/Dev/Desktop/Projetos Pessoais/Python Hashtag/Curso-de-Python/produtos.csv")
print(tabela)

# Função para localizar na tabela as informações 
# linha = autoincrementável
# "codigo" = nome da coluna

tabela.loc[linha, "codigo"]