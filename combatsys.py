import random

#bulbasaur = {'vida': 200, 'ataqueb': 20}

#vida - ataque ou metade do ataque = dano
def atacar(x, y):
    dano = random.randint(y['ataqueb'] // 2, y['ataqueb'])
    vida_restante = x['vida'] - dano
    print(f'você deu {dano} de dano!')
    return vida_restante
