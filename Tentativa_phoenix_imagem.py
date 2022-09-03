#
################################################################################
# aumentar fonte notepad++ ctrl mouse whell up
# Tentando clicar em folha Phoenix
# Início em 11/8/2022 ultima mexida 2/9/2022
# Rodar com Folha Phoenix aberto
################################################################################
#

import pyautogui
import time
pyautogui.PAUSE = 0.5
sistema_desejado = (283, 20)
botao_fenix = 'Ativar.png'
pyautogui.moveTo(sistema_desejado, duration=1)
time.sleep(0.5) #Aguardar meio segundo
pyautogui.click()
#fenix = pyautogui.locateCenterOnScreen(botao_fenix)
time.sleep(1)
pyautogui.moveTo(botao_fenix)
#print("*** passei pelo botao_fenix ***")
time.sleep(0.5)
pyautogui.click()
# ***** PARA 15/08/2022 *****
################################################################################
# CADASTRO EMPRESAS
################################################################################
#
botao_cadastro_empresas = 'CadastroEmpresas.png'
time.sleep(1)
pyautogui.moveTo(botao_cadastro_empresas, duration=1)
#print("*** passei pelo botao_cadastro_empresas ***")
time.sleep(0.5)
pyautogui.click()
#
################################################################################
# INSERIR
################################################################################
#
#cria botao
botao_inserir = 'Inserir.png'
#move to centro do botao
time.sleep(1)
pyautogui.moveTo(botao_inserir, duration=1)
#clica no botao
#print("*** passei pelo botao_inserir ***")
time.sleep(0.5)
pyautogui.click()
#
################################################################################
# BUSCAR
################################################################################
#
#cria botao
botao_buscar = 'buscar.png'
#move to centro do botao
time.sleep(1)
pyautogui.moveTo(botao_buscar, duration=1)
#clica no botao
time.sleep(0.5)
pyautogui.click()
#
################################################################################
# CONSULTAR 1 - Nesta tela só vai por pyautogui
# pesquisa de cnpj -> sou humano -> clica consultar
################################################################################
#
pyautogui.click(376, 443)
pyautogui.write('20.951.310/0001-07')
pyautogui.press("enter")
pyautogui.click(992, 410)
#
################################################################################
# CONSULTAR 2 - Clica em consultar - Point(x=389, y=547)
################################################################################
#
botao_consultar = 'consultar.png'
time.sleep(1)
pyautogui.moveTo(botao_consultar, duration=1)
time.sleep(0.5)
pyautogui.click()
#
################################################################################
# Importar Dados
################################################################################
#
#cria botao
botao_importar_dados = 'ImportarDados.png'
#move to centro do botao
time.sleep(1)
pyautogui.moveTo(botao_importar_dados, duration=1)
#clica no botao
#print("*** passei pelo botao_importar_dados ***")
time.sleep(0.5)
pyautogui.click()
#
#################################################################################
# Gravar
################################################################################
#
#cria botao
botao_gravar = 'gravar.png'
#move to centro do botao
time.sleep(1)
pyautogui.moveTo(botao_gravar, duration=1)
#clica no botao
#print("*** passei pelo botao_importar_dados ***")
time.sleep(0.5)
pyautogui.click()
#
'''
time.sleep(15)
print(pyautogui.position())
pyautogui.alert("Terminei por enquanto, anote as coordenadas")
'''
pyautogui.alert("Terminei por enquanto")
#
#### fui até gravar mas depois que clica no gravar nao acontece mais nada. Falta verificar o que é preenchimento obrigatório
#### faltam pequenos ajustes.