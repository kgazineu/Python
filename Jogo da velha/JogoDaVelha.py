import random
matriz = []
jogadas = 0
max_jogadas = 9
print('=-'*20)
print('Bem vindo ao jogo da velha.')
print('-='*20)

# GERANDO UMA MATRIZ DE ELEMENTOS VÁZIOS PARA SUBSTITUIR COM AS JOGADAS DO PC E USUARIO
for l in range(3):
    lista = []
    for c in range(3):
        lista.append(' ')
    matriz.append(lista)

def imp():
    global matriz

    print('    0    1    2')
    print("0  ", matriz[0][0], ' | ', matriz[0][1], ' | ', matriz[0][2])
    print('   --------------')
    print("1  ", matriz[1][0], ' | ', matriz[1][1], ' | ', matriz[1][2])
    print('   --------------')
    print("2  ", matriz[2][0], ' | ', matriz[2][1], ' | ', matriz[2][2])
imp()

while jogadas < max_jogadas:
    jogada = [int(x) for x in input().split()]
    matriz[jogada[0]][jogada[1]] = 'X'
    imp()
    jogadas += 1
    i = random.randrange(0, 3)
    j = random.randrange(0, 3)

    if matriz[i][j] != 'X':
        matriz[i][j] = "O"
        imp()
        jogadas += 1

    if matriz[0][0] == matriz[0][1] == matriz[0][2]:
        if matriz[0][2] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][2] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[1][0] == matriz[1][1] == matriz[1][2]:
        if matriz[1][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[1][0] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[2][0] == matriz[2][1] == matriz[2][2]:
        if matriz[2][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[2][0] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[0][0] == matriz[1][0] == matriz[2][0]:
        if matriz[0][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][0] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[0][1] == matriz[1][1] == matriz[2][1]:
        if matriz[0][1] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][1] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[0][2] == matriz[1][2] == matriz[2][2]:
        if matriz[0][2] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[0][2] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[0][0] == matriz[1][1] == matriz[2][2]:
        if matriz[1][1] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[1][1] == 'O':
            print('Você perdeu o jogo :( ')
        break
    elif matriz[0][2] == matriz[1][1] == matriz[2][0]:
        if matriz[2][0] == 'X':
            print('Parabéns, você ganhou o jogo!!')
        elif matriz[2][0] == 'O':
            print('Você perdeu o jogo :( ')
        break