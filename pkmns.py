import random


pkmns = {'bulbasaur' : {'vida': 250, 'ataqueb': 20},
         'charmander' : {'vida': 200, 'ataqueb': 30},
       'squirtle' : {'vida': 225, 'ataqueb': 23}, 'zubat' : {'vida': 150, 'ataqueb': 25},
       'pidgey' : {'vida': 200, 'ataqueb': 20}}

pknames = ["bulbasaur", "charmander", "squirtle", "zubat", "pidgey"]

def random_enemy():
 var = random.choice(pknames)
 inimigo = pkmns[f'{var}']
 print (inimigo)
 return inimigo

def choose_strt():
 print('seja bem vindo ao mundo pokemón, escolha seu inicial')
 print('1 - bulbasaur')
 print('2 - charmander')
 print('3 - squirtle')
 sua_escolha = int(input('qual você deseja?'))
 sua_escolha = pknames[sua_escolha]
 sua_escolha = pkmns[f'{sua_escolha}']
 return sua_escolha