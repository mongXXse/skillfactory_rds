# coding: utf-8


import numpy as np


def game_core(number):
    '''Нам на помощь придет бинарный поиск!'''

    count = 0
    mini, maxi = 1, 100

    while True:
        count += 1
        guess = (mini + maxi) // 2

        if guess == number:
            return count

        if number > guess:
            mini = guess + 1
        else:
            maxi = guess - 1


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print('Ваш алгоритм угадывает число в среднем за {score} попыток'.format(score=score))
    return(score)


if __name__ == '__main__':
    score_game(game_core)
