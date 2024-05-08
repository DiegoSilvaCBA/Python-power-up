import pyautogui

pyautogui.PAUSE = 0.8 # pausa para execução de cada comando

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