import random
import numpy as np

# игра угадай число ПК все днлает сам

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    count = 1
    x, y = 1, 100
   
    predict_number = np.random.randint(1, 101)
    
    if number == predict_number:
       return (count)
    else:
        while number != predict_number:
            if number > predict_number:
                y = number
                number = random.randint(x, y)
                count += 1
            elif number < predict_number:
                y = predict_number
                number = random.randint(x, y)
                count += 1
        return (count)
        
print(f"Количество попыток: {random_predict()}")

def score_game(random_predict) -> int:
    """За какое коичество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_lst = [] # список для количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = 1000) # загадали список чисел
    
    for number in random_array:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst)) #находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return (score)

if __name__ == '__main__':
    score_game(random_predict)