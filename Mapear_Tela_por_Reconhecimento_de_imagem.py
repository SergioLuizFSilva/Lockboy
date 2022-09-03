#
################################################################################
# aumentar fonte notepad++ ctrl mouse whell up
# Mapear Tela por Reconhecimento de imagem
# Python DS
# Início em 9/8/2022
################################################################################
#
import pyautogui
import time
pyautogui.PAUSE = 0.5
# fazer script pra chegar no pythin DS ->
# Canal python DS - https://www.youtube.com/c/PythonDS
#meia-tela primeira aba Point(x=1157, y=24)
#meia-tela segunda aba  Point(x=1462, y=31)
videoDesejado = (1462, 31)
botao_curtir = 'like1.png'
termo = 'INSCREVA-SE NO CANAL Python DS'
#Passo 1: Acessar vídeo
pyautogui.moveTo(videoDesejado, duration=1)
time.sleep(0.5) #Aguardar meio segundo
pyautogui.click()
#Função realiza reconhecimento da imagem desejada
curtir = pyautogui.locateCenterOnScreen(botao_curtir)
#Passo 3: Acessar resultado
time.sleep(1)
#Move para o centro da imagem reconhecida
pyautogui.moveTo(curtir)
print("*** passei pelo move to curtir ***")
time.sleep(0.5)
pyautogui.click()
print("*** passei pelo click ***")
time.sleep(30)
print(pyautogui.position())
pyautogui.alert("Terminei por enquanto, anote as coordenadas")
#Point(x=1034, y=583)
