#Aplicação criada para marcar as pessoas para responder o formulário
#Criado por Eduardo Miranda e Gustavo Martins
#Para executar basta instalar o pyautogui 
# usando o comando "pip install pyautogui"
#E mudar a quandidade de pessoas que quer marcar

from time import sleep
import pyautogui as py
quantidadeDePessoas = 107
sleep(5)
for i in range(1,quantidadeDePessoas+1,1):
    py.write("@")
    for j in range(i):
        py.press('down')
    py.press('tab')
