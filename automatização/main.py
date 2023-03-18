# Programa de automatização de processos, como exemplo chamados que eu faço no trabalho (numero de suporte, nome e problemas são ficticios)
# Atenção a detalhes, para que o programa consiga identificar oque é cada coisa é necessario estar atento a alguns detalhes que são
# 1 - Deve-se SEMPRE utilizar o "-" para separar cada campo a ser preenchido
# 2 - O modelo que deve ser sempre escrito é "numero_suporte - nome_cliente - problema_cliente" no texto
# 3 - A algumas falhas mas nada que o tempo não resolva melhorando o programa
# Personalize com suas preferencias e utilizações do dia a dia, seja criativo e use com sabedoria.

# Ver também a velocidade que podem ser executadas as tarefas e se podem ser mais rapidas - VER ISSO!!
# Futuramente criar uma interface visual - VER ISSO!!
# Tentar fazer que ao terminar o chamado (ou qualquer outra coisa) exclua a linha que foi adicionada - VER ISSO!!
# Descobrir algum jeito de fazer o programa sempre ir atualizando toda vez que é adicionado alguma coisa na lista - VER ISSO!!
# Tentar deixar mais ituitivo o possivel e simplificar as coisas para ser mais facil de configurar, talvez adicionar uma coisa de deixar fixo o botão ou coisa a ser feita sem precisar mandar as coordenadas manualmente - VER ISSO!!


# Ass: Vitor Henrique 17/03/2023

import pyautogui
from time import sleep, time




# 2 -  ver os chamados e preencher
with open ('automatização/chamados.txt', 'r') as arquivo:
    for linha in arquivo:
        numero_suporte = linha.split('-')[0]
        nome_cliente = linha.split('-')[1]
        problema_cliente = linha.split('-')[2]
        # 1 -  dar f6 para limpar o formulario
        pyautogui.click(656,262,duration=2) 
        pyautogui.press('f6')
        # 	2.1 - clicar no numero do suporte
        pyautogui.click(431,181,duration=3)
        pyautogui.write(numero_suporte)
        # 	2.2 - clicar no nome
        pyautogui.click(652,242,duration=3)
        pyautogui.write(nome_cliente)
        # 	2.3 - clicar no problema
        pyautogui.click(514,481,duration=1)
        pyautogui.write(problema_cliente)
        # 	2.4 - clicar no tecnico
        pyautogui.click(886,536,duration=2)
        pyautogui.write('25')
        #  2.5 - clicar para imprimir contrato
        pyautogui.click(950,161,duration=1)
        # clica no programa de impressora
        # pyautogui.click(466,763,duration=20)
        # clica na impressora
        pyautogui.click(21,64,duration=18)
        # clica para alterar a impressora
        pyautogui.click(260,167,duration=2)
        # clica na hp 
        pyautogui.click(249,188,duration=2)
        # vai na parte de configurações
        pyautogui.click(427,169,duration=2)
        # vai em finalizações
        pyautogui.click(307,169,duration=2)
        # vai em imprimir nos dois lados
        pyautogui.click(140,290,duration=2)
        # clica em ok
        pyautogui.click(519,643,duration=2)
        # clica para imprimir
        pyautogui.click(356,407,duration=2)
        # clica em olcultar o pop up
        pyautogui.click(565,280,duration=5)
        # fecha a janela de impressão
        pyautogui.click(682,15,duration=2)
        sleep(2)
