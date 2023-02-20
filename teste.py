import random
import combatsys


def atacar(x, y):
    vida_restante = x['vida'] - random.randint(y['ataqueb'] // 2, y['ataqueb'])
    return vida_restante


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
    vida_restante = atacar(inimigo, seupkmn)
    inimigo['vida'] = vida_restante
    print('Vida restante:', vida_restante)
    print (inimigo)