#importacoes
from operator import index
import sys
import time
from random import *
from funcoes import *
from collections import *

def print_slow(str): #Funcao pega no stackoverflow, para colocar slow entre os prints
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)  

#importacao das cores
from colorama import init, Fore,Style #importacao pega no stackoverflow, para colocar cor no jogo
import random
init()

#carrega as palavras e as armazena em uma lista
lista_vocabulario = []
arquivo_texto = open(r"c:\Users\Alexandre Wever\DevLife\PROJETOS\Descobrindo a palavra\palavras.txt", encoding="utf-8")
for palavra in arquivo_texto:
    lista_vocabulario.append(palavra.strip())
    
jogo = True
ja_tentou = []
palavras_cinco = [word for word in lista_vocabulario if len(word) == 5] #palavras da lista do alfabeto dado pelo github do projeto, so aceita as 5 primeiras letras
jogadas = 0
teclado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("\n")
print_slow( """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::
""")
print("\n")
print_slow('Bem vind@ ao jogo DESCOBRINDO A PALAVRA')
print()
print_slow('Você precisa acertar a palavra em 6 tentativas')
print()
print_slow('Para te ajuda vamos te dar algumas dicas:')
print()
print_slow(Fore.GREEN + 'Se a letra estiver verde, ela está presente na palavra e se encontra na posição correta'+ Style.RESET_ALL)
print()
print_slow(Fore.YELLOW + 'Se a letra estiver amarela, ela está presente na palavra, porém não se encontra na posição correta'+ Style.RESET_ALL)
print()
print_slow(Fore.BLACK  + 'Se a letra estiver sem nehuma cor, ela não está presente na palavra'+ Style.RESET_ALL)
print()
print_slow(Fore.BLUE+ """
        ,---,---,---,---,---,---,---,---,---,---,
        | Q | W | E | R | T | Y | U | I | O | P |
        ',--',--',--',--',--',--',--',--',--',--'
         | A | S | D | F | G | H | J | K | L | 
         '-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'---'
           | Z | X | C | V | B | N | M |          
           '---'---'---'---'---'---'---'
       """+ Style.RESET_ALL)
print("\n")

while jogo:
        #tentativas de acertar
       
        
        #escolha uma palavra
        palavra = random.choice(palavras_cinco)
        
        while jogadas <= 6:
            jogadas = jogadas + 1
            print("Escreva uma palavra de 5 letras!\n")
            while True:
                print("\n")
                tentativas = input().lower()
                if tentativas not in palavras_cinco:
                    print("\n")
                    print("Por favor digite um termo válido.(Não deve conter espaços, números e caracteres especiais)") 
                else:
                    break  

            #normaliza os textos
            tentativa_normalizada = remove_acentos(tentativas)  

            # Sobrepoem o ultimo input colocado no terminal e ja da com as cores, codigo procurado no youtube
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            #da as cores para as letras e checa  a repeticao delas 
            repeticao = repeticao_letras(palavra,tentativas)
            print("\n")
            print(repeticao)

            # ver cores no teclado
            print("\n")
            cores_teclado = teclado_colorido(tentativa_normalizada,palavra,teclado)
            for elem in cores_teclado:
                sys.stdout.write(elem + '     ') 
            
            # Sobrepoem o ultimo input colocado no terminal e ja da com as cores, codigo procurado no youtube
            print("\n")
            sys.stdout.write('\x1b[1B')
            sys.stdout.write('\x1b[2S')
            
            
            if palavra == tentativa_normalizada:
                print("\n")
                print_slow(Fore.GREEN + "PARABÉNS VOCÊ VENCEU!" + Fore.RESET)
                print()
                print_slow(Fore.GREEN + f'Você acertou em {jogadas} jogadas' + Fore.RESET)
                print()
                print()
                pergunta_reset = input('Deseja recomeçar' '[S]/[N]' ).upper().strip()
                print()
                if pergunta_reset == 'S':
                    palavra = random.choice(palavras_cinco)
                    jogadas = 0
                    teclado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                else:
                    break
            elif jogadas == 6:
                print("\n")
                print_slow(Fore.RED + "QUE PENA VOCÊ PERDEU!" + Fore.RESET)
                print()
                print_slow(Fore.RED + f"A palavra era [{palavra}]!" + Fore.RESET)
                print()
                print()
                pergunta_reset = input('Deseja recomeçar' '[S]/[N]' ).upper().strip()
                print()
                if pergunta_reset == 'S':
                    palavra = random.choice(palavras_cinco)
                    jogadas = 0
                    teclado = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                else:
                    break 
        break      
