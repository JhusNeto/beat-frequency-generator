import Audio
import Graficos

print('\t\t\tFREQUENCIA DE BATIDA E INTERFERENCIA DE ONDA\n')
print('NESTE SCRIPT ESTAO DISPONIVEIS AS OPCOES DE VISUALIZACAO DE GRAFICOS E EXECUCAO DE SONS DE SINAIS SENOIDAIS, DADAS DUAS FREQUENCIAS.')

key = 1
while key ==1:
    choice = int(input('DESEJA VER OS GRAFICOS (1) OU OUVIR OS SINAIS (2)? 3 PARA SAIR\n'))
    if choice == 1:
        Graficos.iniciaGraficos()
    elif choice == 2:
        Audio.Inicia()
    elif choice == 3:
        key = 0

#Audio.Inicia()
#Graficos.iniciaGraficos()
