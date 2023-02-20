import random
import combatsys


def atacar(x, y):
    vida_restante = x['vida'] - random.randint(y['ataqueb'] // 2, y['ataqueb'])
    return

#testando combate bulbasaur vs charmander
#fazer dicionário com vários outros dicionários com a base dos pokemóns
#e randomizar os status através do lvl

bulbasaur = {'vida': 200, 'ataqueb': 20}
charmander = {'vida': 200, 'ataqueb': 25}

inimigo = bulbasaur
seupkmn = charmander

print('1 - atacar')
print('2 - habilidades (wip)')
print('3 - mochila (wip)')
print('4 - fugir')


while True:
 act = int(input('O que você deseja fazer? '))
 if act == 1:
    vida_restante = combatsys.atacar(inimigo, seupkmn)
    print (vida_restante)