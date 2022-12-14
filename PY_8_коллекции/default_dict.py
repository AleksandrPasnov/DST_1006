from collections import OrderedDict, defaultdict, OrderedDict

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)] 
"""Создадим список из кортежей, ФИО и № Группы"""

groups = dict() # создадим пустой словарь

for x, y in students: # Проверяем, есть ли уже эта группа в словаре
    if y not in groups: # если нет создаем для нее пустой список
        groups[y] = list()
    groups[y].append(x)
"""Сохраним эти данные в словаре, в котором ключами будут номера групп, 
а элементами — списки студентов """

print(groups) # {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']}

"""В данном коде в цикле for происходит распаковка кортежа: 
в переменные цикла student и group попадают первый и второй 
элементы кортежей из списка students. То есть 
на первой итерации цикла в переменной student содержится строка 'Ivanov', 
а в переменной group — целое число 1. 
На второй итерации цикла в переменной student содержится строка 'Smirnov', 
а в переменной group — целое число 4. И так далее.

Обратите внимание, что для решения этой задачи нам потребовался 
шаг с проверкой наличия номера группы в словаре. 
Если номера группы не было, для этой группы мы создавали новый список в словаре. 
Без шага проверки мы бы натолкнулись на KeyError"""

groups_1 = defaultdict(list)

"""Для этого существует объект defaultdict из модуля collections. 
Он позволяет задавать тот тип данных, который хранится в словаре по умолчанию 
(в нашем случае это должен быть список). Это бывает удобно в том случае, 
если приходится заполнять одну и ту же структуру данных, 
экземпляр которой должен храниться по каждому ключу в словаре.
Например, чтобы сохранить информацию о колебании курсов валют за последний месяц, 
можно создать словарь из валютных пар (USD/RUB, EUR/RUB и т. д.), 
а по ключам разместить списки из стоимости валюты по курсу ЦБ за последние 30 дней. 
В таком словаре по каждому ключу должен быть доступен список.
Создадим defaultdict, в котором при обращении по несуществующему ключу 
будет автоматически создаваться новый список. 
Для этого при создании объекта defaultdict в круглых скобках передадим параметр list:
Обратите внимание, что в скобках мы передаём именно указатель на класс объекта 
(например list; также можно было бы применить set, dict) без круглых скобок, 
которые используются для создания нового экземпляра объекта. """

for st, gr in students:
    groups_1[gr].append(st)
 
print(groups_1) # defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})
"""В выводе есть небольшое отличие от обычного словаря: 
печатаются не только элементы словаря, но и само название объекта defaultdict, 
а также класс объекта, который задан по умолчанию. В данном случае это <class 'list'>. """

from collections import OrderedDict
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages = OrderedDict(data)
print(ordered_client_ages)
# По результатам 3 повторов получились вот такие результаты:
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
"""Специальный словарь, который гарантирует сохранение ключей в порядке их добавления, называется OrderedDict"""

