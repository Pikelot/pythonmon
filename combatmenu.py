import combatsys
import random



def combate(inimigo, seupkmn):


 while True:
  print('1 - atacar')
  print('2 - habilidades (wip)')
  print('3 - mochila (wip)')
  print('4 - fugir')
  act = int(input('O que você deseja fazer? '))
  if act == 1:
    vida_restante = combatsys.atacar(inimigo, seupkmn)
    inimigo['vida'] = vida_restante
    print('Vida restante:', vida_restante)