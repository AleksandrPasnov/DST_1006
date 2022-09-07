import numpy as np
import collections
from collections import Counter
c = Counter() # создали объект типа counter (счетчик)

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']

for car in cars:
    c[car] += 1 # считаем значения через цикл

count = Counter(cars) 
""" создаем счетчик и передаем сразу итер. объект, 
    как аргумент, в котором необходимо посчитать значения """

print(count) # Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})

print(count["black"]) # 3
"""Узнать, сколько раз встретился конкретный элемент, 
    можно обратившись к счётчику по ключу как к обычному словарю"""

print(count['purple']) # 0
""" Если обратиться к счётчику по несуществующему 
    ключу, то, в отличие от словаря, ошибка KeyError не возникнет """

print(sum(count.values())) # 9
"""Узнать сумму всех значений в объекте Counter можно, 
    воспользовавшись следующей конструкцией"""

print()

cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']
""" Создадим два списка, и к ним счетчики"""

counter_moscow = Counter(cars_moscow) # Counter({'black': 4, 'yellow': 3, 'white': 2})
counter_spb = Counter(cars_spb) # Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})

print(counter_moscow + counter_spb) # Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})

print(counter_moscow) # Counter({'black': 4, 'yellow': 3, 'white': 2})
print(counter_spb) # Counter({'white': 3, 'red': 2, 'black': 2, 'yellow': 2})
 
counter_moscow.subtract(counter_spb) 
"""Чтобы узнать разницу между объектами Counter, 
необходимо воспользоваться функцией subtract, 
которая меняет тот объект, к которому применяется. 
В примере выше из значений, посчитанных для Москвы, 
вычитаются значения, посчитанные для Санкт-Петербурга """

print(counter_moscow) # Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

print(*counter_moscow.elements()) # black black black black white white yellow yellow yellow
"""Чтобы получить список всех элементов, 
которые содержатся в Counter, используется функция elements(). 
Она возвращает итератор, поэтому, чтобы напечатать все элементы, распакуем их с помощью *"""

print(list(counter_moscow)) # ['black', 'white', 'yellow']
"""Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list()"""

print(dict(counter_moscow)) # {'black': 4, 'white': 2, 'yellow': 3}
"""С помощью функции dict() можно превратить Counter в обычный словарь"""

print(counter_moscow.most_common()) # [('black', 4), ('yellow', 3), ('white', 2)]
"""Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости"""

print(counter_moscow.most_common(2)) # [('black', 4), ('yellow', 3)]
"""В неё также можно передать значение, 
которое задаёт желаемое число первых наиболее частых элементов, например, 2"""

counter_moscow.clear()
"""функция clear() позволяет полностью обнулить счётчик"""