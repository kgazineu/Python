from random import randint

options = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0, 2)

print('=-'*11)
print(' BEM VINDO AO JOKEMPÔ')
print('-='*11)

nome = str(input('Digite seu nome para começarmos o jogo: '))

print('''Suas opções são
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')

jogada = int(input('Bem vindo {}, determine a sua jogada: '.format(nome)))

print('-='*22)
print('O computador jogou {}'.format(options[bot]))
print('Você jogou {}'.format(options[jogada]))
print('=-'*22)

if bot == 0: # escolheu pedra
    if jogada == 0:
        print('EMPATE, JOGUE NOVAMENTE')
    elif jogada == 1:
        print('{} GANHOU!!!'.format(nome))
    elif jogada == 2:
        print('{} PERDEU! TENTE NOVAMENTE..'.format(nome))
    else:
        print('Jogada invalida!')
elif bot == 1: # escolheu papel    
    if jogada == 0: 
        print('{} PERDEU! TENTE NOVAMENTE..'.format(nome))
    elif jogada == 1:
        print('EMPATE, JOGUE NOVAMENTE')
    elif jogada == 2:
        print('{} GANHOU!!!'.format(nome))
    else:
        print('Jogada invalida!')

elif bot == 2: # escolheu tesoura
    if jogada == 0: 
        print('{} GANHOU!!!'.format(nome))
    elif jogada == 1:
        print('{} PERDEU! TENTE NOVAMENTE..'.format(nome))
    elif jogada == 2:
        print('EMPATE, JOGUE NOVAMENTE')
    else:
        print('Jogada invalida!')
