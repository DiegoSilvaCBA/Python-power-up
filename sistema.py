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

tabela = pandas.read_csv("produtos.csv")


# Cadastrar produtos

for linha in tabela.index:  # passa a linha da tabela

    codigo = str(tabela.loc[linha, "codigo"])

    time.sleep(2.0)

    pyautogui.click(x=427, y=260)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(10000) # pra arrastar a tela toda pra cima e começar a cadastrar o próximo produto
