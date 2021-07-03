# Beat Frequency Generator ∿

## ESTRUTURA:

Para melhor organização de funções, o processo foi dividido em 3 módulos - arquivos que contêm definições e instruções da linguagem:

- *Graficos.py*
- *Audio.py*
- *FINAL.py*

## Módulo *Graficos.py*:

- Plota os gráficos das senoides
- Composto pelo método *iniciaGraficos()*, que tem como parâmetros:
  - Limite de tempo (*a*) e frequências 1 e 2 (*f1* e *f2*) 
  - Composto por um *loop* *“while”*, que contém as opções dadas ao usuário sobre qual gráfico deseja visualizar

## Módulo *Audio.py*:

- Gera sinais - na forma de *arrays*, cria arquivos *.wav* correspondentes aos sinais e executa esse arquivo
- Composto pela classe:
  - *SoundFile()*, que contém os métodos:
    - *<u> __</u>init<u> __</u>()*, que define os par metros básicos para o arquivo de áudio
    - *write()*, que grava o sinal no arquivo de áudio
- Composto pelas funções: 
  - *geraSenoide()*, que recebe os parâmetros: frequência, duração, valor de pico e taxa de amostragem e retorna os valores do sinal
  - *geraSenoide12(),* que recebe os mesmos par metros de gerasenoide e retorno os valores do sinal
- E pelos métodos:
  - *playFile(),* que executa o arquivo *.wav* gerado por *SoundFile*
  - *Inicia(),* que é composta por um *loop “while”*, que contém as opções dadas ao usuário sobre qual gráfico deseja visualizar

## Módulo *Final.py*:

- Gera um menu ao usuário, com as opções:
  - *DESEJA VER OS GRÁFICOS? (1)*
  - *OU OUVIR OS SONS? (2)*
  - *3 PARA SAIR*
- Caso o usuário digite 1:
  - Faz-se o uso do módulo *Gaficos.py*, solicitando-se os parâmetros de:
    - Limite de tempo
    - Frequência 1
    - Frequência 2
  - Geram-se os gráficos, dando ao usuário as opções:
    - 1
    - 2
    - 12 (FREQUÊNCIAS 1 E 2 SOBREPOSTAS)
    - 3 (SAIR)

- Caso o usuário digite 2:
  - Faz-se o uso do módulo *Audio.py*, solicitando-se os parâmetros de:
    - Duração
    - Frequência 1
    - Frequência 2
  - Criam-se os arquivos *sin1.wav*, *sin2.wav* e *sin12.wav,* dando ao usuário as opções:
    - 1
    - 2
    - 12 (FREQUÊNCIAS 1 E 2 SOBREPOSTAS)
    - 3 (SAIR)