#
################################################################################
# CONSULTAR 1 - Nesta tela só vai por pyautogui
# pesquisa de cnpj -> sou humano -> clica consultar
################################################################################
#
import pyautogui
import time
pyautogui.PAUSE = 2
#
pyautogui.click(376, 443)
pyautogui.write('20.951.310/0001-07')
pyautogui.press("enter")
pyautogui.click(992, 410)
#
'''
time.sleep(15)
print(pyautogui.position())
pyautogui.alert("Terminei por enquanto, anote as coordenadas")
'''
#

