import pyautogui  # para instalar: pip install pyautogui
import time

pyautogui.PAUSE = 1.0  # pausa para execução de cada comando

pyautogui.click  # click: para clicar em uma posição na tela
pyautogui.write  # write: para escrever um texto
pyautogui.press  # press: para pressionar uma tecla

# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no sitema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pausa para execução do próximo comando nesse ponto específico
time.sleep(2.0)

# Fazer login
pyautogui.click(x=434, y=375)  # clicando no local específico
pyautogui.write("seu_email@gmail.com")
pyautogui.press("tab")  # passa pro próximo campo de formulário
pyautogui.write("12345")
pyautogui.press("tab")  # passa pro butão logar
pyautogui.press("enter")
time.sleep(2.0)


# Abrir/Importar a base de dados de produtos para cadastrar

import pandas   # instalar: pip install pandas numpy openpyxl

tabela_produtos = pandas.read_csv("produtos.csv")