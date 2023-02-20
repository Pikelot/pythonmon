
import jogo
import pkmns

import combatmenu

######introdução##########
jogo.intro()
seu_inicial = pkmns.choose_strt()
#########################

print('o que você deseja fazer?')
print('1 - procurar por inimigos')
print('2 - andar pelo mapa (wip)')

while True:
 ação = int(input('o que farás?'))
 if ação == 1:
  inimigo = pkmns.random_enemy
  print(f'você encontra um {inimigo} selvagem!!')
  combatmenu.combate(inimigo, seu_inicial)

