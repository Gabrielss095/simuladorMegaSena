#SIMULADOR DE JOGOS DA MEGA SENA

from random import randint
from time import sleep
print('='*60)
print()
print(f'\033[34:1m {"SEJA BEM VINDO AO SIMULADOR DE JOGOS DA MEGA SENA":^60}\033[m')
print()
print('='*60)

Quant = int(input('Quantos jogos você deseja fazer? '))
Quantjogos = []
tot = 0
for c in range(0, Quant):
    jogo = [randint(1, 60), randint(1, 60), randint(1, 60),
            randint(1, 60), randint(1, 60), randint(1, 60)]
    tot = Quant * jogo
    Quantjogos.append(jogo[:])
    sleep(1)
    print(f'{c+1}ª JOGO: ', end='')
    print(jogo)
    sleep(1)
    print('.....')

    Quantjogos.clear()
print(f'\033[31:1m{"BOA SORTE!!!":^20} \033[m')
