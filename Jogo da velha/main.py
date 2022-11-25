import random
import os

lista = []
matriz = []
ganhador = False
vez = 0

# Gerando uma matriz de elementos vazios para ser a 'velha'

for l in range(3):
    lista = []
    for c in range(3):
        lista.append(' ')
    matriz.append(lista)

# Função responsavel por imprimir a 'velha'

def imprimir_velha():
    print("\n" + '    0     1     2')
    print("0  ", matriz[0][0], ' | ', matriz[0][1], ' | ', matriz[0][2])
    print('   --------------')
    print("1  ", matriz[1][0], ' | ', matriz[1][1], ' | ', matriz[1][2])
    print('   --------------')
    print("2  ", matriz[2][0], ' | ', matriz[2][1], ' | ', matriz[2][2] + "\n")

# Função responsavel por quem ganha e quem perde

def winner():
    global ganhador
    if matriz[0][0] == matriz[0][1] == matriz[0][2]:
        if matriz[0][2] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][2] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[1][0] == matriz[1][1] == matriz[1][2]:
        if matriz[1][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[1][0] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[2][0] == matriz[2][1] == matriz[2][2]:
        if matriz[2][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[2][0] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[0][0] == matriz[1][0] == matriz[2][0]:
        if matriz[0][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][0] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[0][1] == matriz[1][1] == matriz[2][1]:
        if matriz[0][1] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][1] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[0][2] == matriz[1][2] == matriz[2][2]:
        if matriz[0][2] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][2] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[1][1] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[1][1] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True
    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[2][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[2][0] == 'O':
            print('Você perdeu o jogo :( ')
        ganhador = True



def jogo():
    winner()
    jogadas = 0
    imprimir_velha()
    i = int(input("Determine a linha da sua jogada: "))
    j = int(input("Determine a coluna da sua jogada: "))
    matriz[i][j] = "X"
    vez = 1
    os.system("cls")
    
    while jogadas < 9 and ganhador == False:
        if vez == 1 and  ganhador == False:
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
            if matriz[l][c] == " ":
                matriz[l][c] = "O"
                vez = 0
                jogadas += 1
                imprimir_velha()

        elif vez == 0 and ganhador == False:
            i = int(input("Determine a linha da sua jogada: "))
            j = int(input("Determine a coluna da sua jogada: "))
            if matriz[i][j] == " ":
                matriz[i][j] = "X"
                vez = 1 
                jogadas += 1
                imprimir_velha()
            #print(matriz[0][0] + matriz[0][1] + matriz[0][2])
            os.system("cls")      
        


def main():
    iniciar = input("Deseja jogar? (s/n) " + "\n")
    if iniciar == "s" or iniciar == "S":
        print('=-'*15)
        print('  ' + 'Bem vindo ao jogo da velha')
        print('-='*15 + "\n")
        print("Jogo da velha tradicional, para escolher \na posição desejada o jogador vai selecionar \na linha e coluna desejada para jogar \n \nPor exemplo '0 0' ou '0 1'. ")
        jogo()

    elif iniciar == "n" or iniciar == "N":
        print("Até a próxima!! :D ")

    else:
        print("O valor inserido não corresponde às alternativas.\nTente novamente!")

main()