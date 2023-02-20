import keyboard
import jogo

print('1 - Iniciar')
print('2 - Sair')




while True:
    if keyboard.read_key() == "1":
        jogo.intro()
        break
    if keyboard.read_key() == "2":
        break