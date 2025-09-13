import numpy as np

number = np.random.randint(1, 101)  # let's guess the number
count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number from 1 to 100: '))
    
    if predict_number > number:
        print('The number must be less!')
    elif predict_number < number:
        print('The number must be higher!')
    else:
        print(f'You guessed the number in {count} attempts! This number = {number}')
        break                       # end of game, exit from loop