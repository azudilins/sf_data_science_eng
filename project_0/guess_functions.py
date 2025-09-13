"""
Guess the Number Game.
The computer thinks of and guesses the number itself.
"""
import numpy as np

def user_predict():
    """Guess the number manually
    """
    number = np.random.randint(1, 101)                       # let's guess the number
    count = 0

    while True:
        count += 1
        predict_number = int(input('Guess the number from 1 to 100: '))
        print('Entered number:', predict_number)
        
        if predict_number > number:
            print('The number must be less!')
            print()
        elif predict_number < number:
            print('The number must be higher!')
            print()
        else:
            print(f'You guessed the number in {count} attempts! This number = {number}')
            break                                            # end of game, exit from loop


def random_predict(number:int=1) -> int:
    """Guess the number randomly

    Args:
        number (int, optional): The Hidden Number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)           # estimated number
        
        if number == predict_number:
            break                                            # exit the loop if you guessed right
    
    return count


def moving_predict(number:int=1) -> int:
    """First, we set any random number, and then decrease or increase
    it depending on whether it is greater or less than the desired one.
    The function accepts the guessed number and returns the number of attempts.

    Args:
        number (int, optional): The Hidden Number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def advanced_predict(number:int=1) -> int:
    """We set the average number between the minimum and maximum possible values.
    Possible values decreases or increases - depending on whether entered value is greater or less than the desired one.
    The function accepts the guessed number and returns the number of attempts.

    Args:
        number (int, optional): The Hidden Number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    min_possible = 0
    max_possible = 101
    
    while True:
        count += 1
        predict = int((min_possible+max_possible) / 2)
        
        if number > predict:
            min_possible= predict
        elif number < predict:
            max_possible = predict
        else:
            return count


def score_game(predict_method) -> int:
    """How many attempts on average out of 1000 approaches does our algorithm guess?

    Args:
        predict_method (func): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []                                            # list to save number of attempts
    np.random.seed(1)                                        # we fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size = (1000))  # guessed a list of numbers
    
    for number in random_array:
        count_ls.append(predict_method(number))
    
    score = int(np.mean(count_ls))                           # find the average number of attempts
    print(f'Your algorithm guesses the number on average in: {score} attempts')