import random
#bulbasaur = {'vida': 200, 'ataqueb': 20}

#vida - ataque ou metade do ataque = dano
def atacar(x, y):
    vida_restante = x['vida'] - random.randint(y['ataqueb'] // 2, y['ataqueb'])
    print(vida_restante)
    return vida_restante
