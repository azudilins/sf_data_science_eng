"""
Guess the Number Game.
The computer thinks of and guesses the number itself.
"""
import numpy as np


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
    
    return(count)


def score_game(random_predict) -> int:
    """How many attempts on average out of 1000 approaches does our algorithm guess?

    Args:
        random_predict (func): guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []                                            # list to save number of attempts
    np.random.seed(1)                                        # we fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size = (1000))  # guessed a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))                           # find the average number of attempts
    print(f'Your algorithm guesses the number on average in: {score} attempts')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)