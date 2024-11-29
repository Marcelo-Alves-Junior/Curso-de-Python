# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer Login
# Passo 3: Importar a base de dados do Produto 
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir cadastro para todos os produtos

import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=768, y=371)
pyautogui.write("teste@teste.com")
pyautogui.click(x=768, y=371)
pyautogui.write("teste_senha")
