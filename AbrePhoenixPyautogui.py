# Abrir o Phoenix
# Integrações -> Importações de Dados -> Cadastros Gerais
# 1-Escreve Folha Phoenix
# 2- Clica com direito em Folha Phoenix
#
#
################################################################################
# Ultima mexida em 8/8/2022 16:13 cnpj de teste 20.951.310/0001-07
################################################################################
#
import pyautogui
import time
pyautogui.PAUSE = 2
#
################################################################################
# 1-Escreve Folha Phoenix
# 1.1 abrir navegador
################################################################################
#
pyautogui.press("winleft")
pyautogui.write("Folha Phoenix")
pyautogui.click (515,542)
# arquivos
time.sleep(22)
pyautogui.click(39,55)
#
#
################################################################################
## botao empresas -> empresas
################################################################################
#
pyautogui.click(73,109)
pyautogui.click(380,109)
#
################################################################################
##botao inserir -> clica cnpj
################################################################################
#
pyautogui.click(376,184)
pyautogui.click(461, 59)
#
################################################################################
# preenche cnpj
################################################################################
#
#pyautogui.write('20.951.310/0001-07')
pyautogui.click(664,68)
#
################################################################################
# pesquisa de cnpj -> sou humano -> clica consultar
################################################################################
#
pyautogui.click(476, 390)
pyautogui.write('20.951.310/0001-07')
pyautogui.press("enter")
pyautogui.click(1025, 364)
pyautogui.click(494, 499)
#
################################################################################
#### importar dados
################################################################################
#
time.sleep(10)
pyautogui.click(850, 714)
#
################################################################################
## gravar
################################################################################
#
pyautogui.doubleClick(1105, 864)
#
#time.sleep(15)
#print(pyautogui.position())
#pyautogui.alert("Terminei por enquanto, anote as coordenadas")
pyautogui.alert("Termino do programa")
