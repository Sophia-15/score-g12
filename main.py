import os
import keyboard

alfabeto = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
  'Y', 'Z'
]

cont = 0
name = ['A', 'A', 'A']

print(' '.join(name))
for i in range(3):
    cont = 0
    while True:
        if keyboard.is_pressed('up'):
            os.system('clear')
            cont -= 1
            name[i] = alfabeto[cont]
            print(' '.join(name))
            
        elif keyboard.is_pressed('down'):
            os.system('clear')
            cont += 1
            name[i] = alfabeto[cont]
            print(' '.join(name))

        elif keyboard.wait('enter'):
            break
            
print(''.join(name))
