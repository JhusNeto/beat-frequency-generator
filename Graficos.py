from pylab import arange, plot, xlabel, ylabel, title, grid, show  #biblioteca de graficos
from numpy import sin, pi


def iniciaGraficos(): #funcao para plotar os graficos das senoides
    print('\t\t-------------VISUALIZACAO DE GRAFICOS-------------\n')    
    a = float(input('Limite de Tempo:\n')) #recebe o valor do tempo
    f1 = float(input('Frequencia 1:\n')) #recebe a frequencia 1
    f2 = float(input('Frequenciia 2:\n')) #recebe a frequencia 2
    zoom = int(input('Quantas vezes de zoom deseja aplicar?\n')) #recebe o zoom desejado pelo usuario
    t = arange (-a, a, 0.0002 ) #define o eixo dos tempos do grafico
    
    y1 = sin((2*pi*f1*t)/zoom) #define a senoide do sinal 1 com zoom
    y2 = sin(2*pi*f2*t/zoom) #define a senoide do sinal 2 com zoom
    y12 = sin((2*pi*f1*t)/zoom)+sin((2*pi*f2*t)/zoom) #define a senoide do sinal 12 (1 e 2 tocados juntos)
    
    key = 1    #define uma variavel para entrar ou sair do loop (key=1 entra =0 sai)
    
    while key == 1: #entra no loop (key=1)
        resp = int(input('Qual grafico deseja ver? (1), (2) ou (12)? 3 para sair\n')) #qual grafico sera plotado e guarda a resposta numa variavel
        if resp == 1: #opcao pelo grafico 1
            plot(t,y1) #define o grafico 1 como sendo de y1 em funcao do tempo t
            xlabel ('Tempo (s)') #rotulo do eixo dos tempos
            ylabel ('Amplitude') #rotulo do eixo das amplitudes
            title ('Frequencia 1') #titulo do grafico 1
            grid (True) #ativa as linhas de grade
            show() #mostra o grafico com as configuracoes definidas acima

        elif resp == 2: #opcao pelo grafico 2
            plot(t,y2) #define o grafico 2 como sendo de y2 em funcao do tempo t
            xlabel ('Tempo (s)') #rotulo do eixo dos tempos
            ylabel ('Amplitude') #rotulo do eixo das amplitudes
            title ('Frequencia 2') #titulo do grafico 2
            grid (True) #ativa as linhas de grade
            show() #mostra o grafico com as configuracoes definidas acima

        elif resp == 12: #opcao pelo grafico 12
            plot(t,y12) #define o grafico 12 como sendo de y12 em funcao do tempo t
            xlabel ('Tempo (s)') #rotulo do eixo dos tempos
            ylabel ('Amplitude') #rotulo do eixo das amplitudes
            title ('Frequencia 12') #titulo do grafico 12
            grid (True) #ativa as linhas de grade
            show() #mostra o grafico com as configuracoes definidas acima

        elif resp == 3: #opcao sair dos graficos
            key = 0 #sai do loop (key=0)
        
        else: #opcao invalida (valor diferente de 1, 2, 12 ou 3)
            print('Valor invalido! Serao plotados os tres graficos') #avisa ao usuario
            #grafico 1
            plot(t,y1) #define o grafico 1 como sendo de y1 em funcao do tempo t 
            xlabel ('Tempo (s)') #rotulo do eixo dos tempos
            ylabel ('Amplitude') #rotulo do eixo das amplitudes
            title ('Frequencia 1') #titulo do grafico 1
            grid (True) #ativa as linhas de grade
            show() #mostra o grafico 1 com as configuracoes definidas acima 
            #grafico 2
            plot(t,y2) #define o grafico 2 como sendo de y2 em funcao do tempo t
            xlabel ('Tempo (s)') #rotulo do eixo dos tempos
            ylabel ('Amplitude') #rotulo do eixo das amplitudes
            title ('Frequencia 2') #titulo do grafico 2
            grid (True) #ativa as linhas de grade
            show() #mostra o grafico 2 com as configuracoes definidas acima
            #grafico 12
            plot(t,y12) #define o grafico 12 como sendo de y12 em funcao do tempo t
            xlabel ('Tempo (s)') #rotulo do eixo dos tempos
            ylabel ('Amplitude') #rotulo do eixo das amplitudes
            title ('Frequencia 12') #titulo do grafico 12
            grid (True) #ativa as linhas de grade
            show() #mostra o grafico 12 com as configuracoes definidas acima
           

#iniciaGraficos() #teste de uso da funcao
