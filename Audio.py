import numpy as np #biblioteca para manipulacao de dados
import wave #biblioteca para leitura e escrita de arquivos .wav
import pyaudio #biblioteca para executar e gravar audios


class SoundFile: #criacao do arquivo de audio
    def __init__(self, sinal, nomeArquivo, taxaAmostragem = 44100): #defincao de parametros
        self.arquivoWav = wave.open(nomeArquivo, 'wb') #define nome do arquivo a ser criado
        self.sinal = sinal.tostring() #define o sinal e o transforma em string
        self.taxaAmostragem = taxaAmostragem #define a taxa de amostragem

    def write(self): #escrita do arquivo
        self.arquivoWav.setnchannels(1) #define o numero de canais (mono ou stereo)
        self.arquivoWav.setsampwidth(2) #define o tamanho das amostras em bytes
        self.arquivoWav.setframerate(self.taxaAmostragem) #define taxa de amostragem
        self.arquivoWav.writeframes(self.sinal) #grava os frames (amostras) no arquivo
        self.arquivoWav.close() #fecha o arquivo e finaliza a operacao de escrita

def playFile(strFileName): #tocar o audio do arquivo gerado por SoundFile

    chunk = 1024 #quantidade de frames que sao lidos a cada iteracao

    f = wave.open(strFileName, 'rb') #define f como a funcao que abre o arquivo

    p = pyaudio.PyAudio() # define p como uma instancia do pyaudio

    stream = p.open(format = p.get_format_from_width(f.getsampwidth()), #abre um arquivo com os parametros dentro dos parenteses
            channels = f.getnchannels(),
            rate = f.getframerate(),
            output = True)

    data = f.readframes(chunk) #le os frames - chunk frames por iteracao

    while data:
        stream.write(data) #escreve os frames no arquivo
        data = f.readframes(chunk)#le proximos frames

    stream.stop_stream() #para de escrever o arquivo
    stream.close() #fecha o arquivo
    p.terminate() #termina a operacao

def geraSenoide(frequencia= 1000, duracao=1, valorPico= 16384, taxaAmostragem=44100): #Gera um array numpy correspondente a uma senoide - usada para sinal 1 e 2
    numeroAmostras = duracao * taxaAmostragem #define o numero de amostras

    periodo = 1.0 / float(frequencia) #define o periodo
    omega = np.pi * 2.0 / periodo #define a frequencia fundamental
    deltaX= 1.0 / float(taxaAmostragem) #gera o sinal senoidal de sinais separados

    tempo = np.arange(start=0, stop= duracao, step= deltaX, dtype=np.float) #define o tamanho do eixo dos tempos
    valorSinal = valorPico * np.sin(tempo * omega) #define o valor do sinal 

    return valorSinal #retorna o valor do sinal

def geraSenoide12(frequencia1= 1000, frequencia2= 1000, duracao=1, valorPico= 16384, taxaAmostragem=44100): #Gera um array numpy correspondente a uma senoide - usada para 12
    numeroAmostras = duracao * taxaAmostragem

    periodo1 = 1.0 / float(frequencia1)
    periodo2 = 1.0 / float(frequencia2)
    omega1 = np.pi * 2.0 / periodo1
    omega2 = np.pi * 2.0 / periodo2
    deltaX= 1.0 / float(taxaAmostragem) #gero o sinal senoidal de dois sinais sobrepostos

    tempo = np.arange(start=0, stop= duracao, step= deltaX, dtype=np.float)
    valorSinal1 = valorPico * np.sin(tempo * omega1)
    valorSinal2 = valorPico * np.sin(tempo * omega2)
    valorSinal12 = valorSinal1 + valorSinal2

    return valorSinal12

#duracao_user = input("Digite a Duracao desejada: ") #usuario define a duracao
#frequencia1_user = input('Digite a Frequencia 1:') #usuario define a frequencia 1
#frequencia2_user =  input('Digite a Frequencia 2:') #usuario define a frequencia 2
def Inicia():
    print('\t\t-------------EXECUCAO DE SONS-------------\n')
    duracao_user = float(input("Digite a Duracao desejada:\n")) #usuario define a duracao
    frequencia1_user = input('Digite a Frequencia 1:\n') #usuario define a frequencia 1
    frequencia2_user =  input('Digite a Frequencia 2:\n') #usuario define a frequencia 2

    data1 = geraSenoide(frequencia = frequencia1_user, #gera sinal 1
            duracao = duracao_user,
            valorPico = 16384,
            taxaAmostragem = 44100)

    data2 = geraSenoide(frequencia = frequencia2_user, #gera sinal 2
            duracao = duracao_user,
            valorPico = 16384,
            taxaAmostragem = 44100)

    data12 = geraSenoide12(frequencia1= frequencia1_user, #gera sinal 12 sobreposicao dos dois anteriores
            frequencia2= frequencia2_user,
            duracao= duracao_user,
            valorPico= 16384,
            taxaAmostragem= 44100)

    sinal1 = np.array(data1, dtype = np.int16) #transforma o sinal 1 num array de inteiros
    sinal2 = np.array(data2, dtype = np.int16) #transforma o sinal 2 num array de inteiros
    sinal12 = np.array(data12, dtype = np.int16) #transforma o sinal 12 num array de inteiros
    #sinal1_list = sinal1.tolist()
    #sinal2_list = sinal2.tolist()
    #sinal3_list = []

    #for elem1, elem2 in zip(sinal1_list, sinal2_list):
    #    sinal3_list.append((elem1 + elem2))

        #sinal3 = np.asarray(sinal3_list)

    key = 1
    while key == 1:
        resp = int(input('QUAL SINAL DESEJA TOCAR? (1). (2), (12)? 3 PARA SAIR\n '))
        if resp == 1:
            file1 = SoundFile(sinal1, 'sin1.wav')
            file1.write()
            playFile('sin1.wav')
            #break
            #resp = int(input('Deseja tocar mais algum sinal? (2) ou (12)?'))
        elif resp == 2:
            file2 = SoundFile(sinal2, 'sin2.wav')
            file2.write()
            playFile('sin2.wav')
            #break
            #resp = int(input('Deseja tocar mais algum sinal? (1) ou (12)?'))
        elif resp == 12:
            file12 = SoundFile(sinal12, 'sin12.wav')
            file12.write()
            playFile('sin12.wav')
            #break
            #resp = int(input('Deseja tocar mais algum sinal? (1) ou (2)?'))
        elif resp == 3:
            key = 0
        else:
            print('Valor invalido! Serao tocados os tres sinais sequencialmente (1, 2 e 12)')
            file1 = SoundFile(sinal1, 'sin1.wav')
            file1.write()
            playFile('sin1.wav')
            file2 = SoundFile(sinal2, 'sin2.wav')
            file2.write()
            playFile('sin2.wav')
            file12 = SoundFile(sinal12, 'sin12.wav')
            file12.write()
            playFile('sin12.wav')
            #break
#print(sinal1[10])
#print(sinal2[10])
#print(sinal12[10])

#Inicia()
