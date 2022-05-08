import sys
import time
from random import *
from collections import *
from colorama import init, Fore, Back, Style #importacao pega no stackoverflow, para colocar cor no jogo
init()
import unicodedata


def print_slow(str): #Funcao pega no stackoverflow, para colocar slow entre os prints
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)       

def remove_acentos(s): #funcao pega no quiz 4 
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


def teclado_colorido(tentativas,palavra,teclado):
    for elem1,elem2 in zip(tentativas,palavra):
        if elem1 == elem2 and elem1 in teclado:
            posicao = teclado.index(elem1)
            teclado[posicao] = Fore.GREEN + elem1 + Fore.WHITE
        elif elem1 != elem2 and elem1 in palavra and elem1 in teclado:
            posicao = teclado.index(elem1)
            teclado[posicao] = Fore.YELLOW + elem1 + Fore.WHITE
        elif elem1 not in palavra and elem1 in teclado:
            posicao = teclado.index(elem1)
            teclado[posicao] = Fore.BLACK + elem1 + Fore.WHITE
    return teclado


SQUARES = {
'palavra_correta': '🟩',
'palavra_presente': '🟨',
'palavra_errada': '⬛'
}

sequencia_wordle = []

def repeticao_letras(palavra,tentativas):
    sequencia_wordle = []
    contador1 = 0
    string_retorno = ''
    if palavra[0] == tentativas[0]:
        if palavra[0] == tentativas[0] and tentativas.count(tentativas[0]) > 1:
            primeira = Fore.GREEN + palavra[0] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
            contador1 = 1
        else:
            primeira = Fore.GREEN + palavra[0] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
    elif palavra[0] != tentativas[0]:
        if tentativas[0] in palavra and tentativas.count(tentativas[0]) == palavra.count(tentativas[0]):
            primeira = Fore.YELLOW + tentativas[0] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
        elif tentativas[0] != palavra[0] and tentativas.count(tentativas[0]) > palavra.count(tentativas[0]):
            primeira = Fore.BLACK + tentativas[0] + Fore.RESET  
            sequencia_wordle.append(SQUARES['palavra_errada'])
        elif contador1 == 0 and tentativas.count(tentativas[0]) > 1 and tentativas[0] in palavra:
            primeira = Fore.YELLOW + tentativas[0] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        elif contador1 == 1 and palavra.count(tentativas[0]) > tentativas.count(tentativas[0]) and tentativas[0] in palavra:
            primeira = Fore.YELLOW + tentativas[0] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        else:
            primeira = Fore.BLACK + tentativas[0] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_errada'])
    
    if palavra[1] == tentativas[1]:
        if palavra[1] == tentativas[1] and tentativas.count(tentativas[1]) > 1:
            segunda = Fore.GREEN + palavra[1] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
            contador1 = 1
        else:
            segunda = Fore.GREEN + palavra[1] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
    elif palavra[1] != tentativas[1]:
        if tentativas[1] in palavra and tentativas.count(tentativas[1]) == palavra.count(tentativas[1]):
            segunda = Fore.YELLOW + tentativas[1] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
        elif contador1 == 0 and tentativas.count(tentativas[1]) > 1 and tentativas[1] in palavra:
            segunda = Fore.YELLOW + tentativas[1] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        elif contador1 == 1 and palavra.count(tentativas[1]) > tentativas.count(tentativas[1]) and tentativas[1] in palavra:
            segunda = Fore.YELLOW + tentativas[1] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        else:
            segunda = Fore.BLACK + tentativas[1] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_errada'])
    
    if palavra[2] == tentativas[2]:
        if palavra[2] == tentativas[2] and tentativas.count(tentativas[2]) > 1:
            terceira = Fore.GREEN + palavra[2] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
            contador1 = 1
        else:
            terceira = Fore.GREEN + palavra[2] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
    elif palavra[2] != tentativas[2]:
        if tentativas[2] in palavra and tentativas.count(tentativas[2]) == palavra.count(tentativas[2]):
            terceira = Fore.YELLOW + tentativas[2] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
        elif contador1 == 0 and tentativas.count(tentativas[2]) > 1 and tentativas[2] in palavra:
            terceira = Fore.YELLOW + tentativas[2] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        elif contador1 == 1 and palavra.count(tentativas[2]) > tentativas.count(tentativas[2]) and tentativas[2] in palavra:
            terceira = Fore.YELLOW + tentativas[2] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        else:
            terceira = Fore.BLACK + tentativas[2] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_errada'])
    
    if palavra[3] == tentativas[3]:
        if palavra[3] == tentativas[3] and tentativas.count(tentativas[3]) > 1:
            quarta = Fore.GREEN + palavra[3] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
            contador1 = 1
        else:
            quarta = Fore.GREEN + palavra[3] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
    elif palavra[3] != tentativas[3]:
        if tentativas[3] in palavra and tentativas.count(tentativas[3]) == palavra.count(tentativas[3]):
            quarta = Fore.YELLOW + tentativas[3] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
        elif contador1 == 0 and tentativas.count(tentativas[3]) > 1 and tentativas[3] in palavra:
            quarta = Fore.YELLOW + tentativas[3] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        elif contador1 == 1 and palavra.count(tentativas[3]) > tentativas.count(tentativas[3]) and tentativas[3] in palavra:
            quarta = Fore.YELLOW + tentativas[3] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        else:
            quarta = Fore.BLACK + tentativas[3] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_errada'])
    
    if palavra[4] == tentativas[4]:
        if palavra[4] == tentativas[4] and tentativas.count(tentativas[4]) > 1:
            quinta = Fore.GREEN + palavra[4] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
            contador1 = 1
        else:
            quinta = Fore.GREEN + palavra[4] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_correta'])
    elif palavra[4] != tentativas[4]:
        if tentativas[4] in palavra and tentativas.count(tentativas[4]) == palavra.count(tentativas[4]):
            quinta = Fore.YELLOW + tentativas[4] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
        elif contador1 == 0 and tentativas.count(tentativas[4]) > 1 and tentativas[4] in palavra:
            quinta = Fore.YELLOW + tentativas[4] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        elif contador1 == 1 and palavra.count(tentativas[4]) > tentativas.count(tentativas[4]) and tentativas[4] in palavra:
            quinta = Fore.YELLOW + tentativas[4] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_presente'])
            contador1 = 1
        else:
            quinta = Fore.BLACK + tentativas[4] + Fore.RESET
            sequencia_wordle.append(SQUARES['palavra_errada'])
    string_retorno = (primeira + ' ' + segunda + ' ' +  terceira + ' ' +  quarta + ' ' +  quinta)
    print(' '.join(sequencia_wordle))
    return string_retorno.upper()
  


 
