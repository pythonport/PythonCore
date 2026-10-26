'''
Code for ludo game.
'''
import random
for i in range(3):
    num = random.randint(1,6)
    print(f"Chance {i+1} - {num}")
    if num == 6 :
        print(f'{num} YOU WON')
        break
else :
    print('HARD LUCK...')