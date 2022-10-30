import pandas as pd
melb_df = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_12_Продвинутые методы Pandas/data_csv/melb_data_fe.csv')

# 1
melb_df['Date'] = pd.to_datetime(melb_df['Date'])
quarters = melb_df['Date'].dt.quarter


# 2
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
max_unique_count = 150
for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')


# 3
# Для сортировки значений в DF по значениям одного или нескольких столбцов используйте метод sort_values()

melb_df.sort_values(by='Price').head(10)

# 4
# Отсортируем таблицу по убыванию, столбец даты продажи объекта Date

melb_df.sort_values(by='Date', ascending=False)

# 5
# Для сортировки по значениям нескольких столбцов необходимо передать названия
# этих столбцов в параметр by в виде списка. При этом важно обращать внимание
# на порядок следования столбцов.

melb_df.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']]

# 6
# Найдём информацию о таунхаусах (Type), проданных компанией (SellerG) McGrath,
# у которых коэффициент соотношения площадей здания и участка (AreaRatio) меньше -0.8.
# Результат отсортируем по дате продажи (Date) в порядке возрастания,
# а после проведём сортировку по убыванию коэффициента соотношения площадей.
# Также обновим старые индексы на новые, установив параметр ignore_index на True.
# Для наглядности результата выберем из таблицы только столбцы Data и AreaRatio:

mask1 = melb_df['AreaRatio'] < -0.8
mask2 = melb_df['Type'] == 'townhouse'
mask3 = melb_df['SellerG'] == 'McGrath'
melb_df[mask1 & mask2 & mask3].sort_values(
    by=['Date', 'AreaRatio'],
    ascending=[True, False],
    ignore_index=True
).loc[:, ['Date', 'AreaRatio']]

# 7
# Произведите сортировку столбца AreaRatio по убыванию.
# При этом индексы полученной таблицы замените на новые.
# Какое значение площади здания находится в строке 1558?

# 8
# Найдите таунхаусы (Type) с количеством жилых комнат (Rooms) больше 2.
# Отсортируйте полученную таблицу сначала по возрастанию числа комнат,
# а затем по убыванию средней площади комнат (MeanRoomsSquare).
# Индексы таблицы замените на новые. Какая цена будет у объекта в строке 18?
mask_1 = melb_df['Type'] == 'townhouse'
mask_2 = melb_df['Rooms'] > 2
res = melb_df[mask_1 & mask_2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'],
    ascending=[True, False],
    ignore_index=True).loc[18, 'Price']

# 9
# В библиотеке Pandas для группировки данных по одному
# или нескольким признакам можно использовать метод groupby().
# Метод groupby() возвращает объект DataFrameGroupBy,
# который хранит в себе информацию о том, какие строки относятся к определённой группе,
# и сам по себе не представляет для нас интереса.
# Однако к этому объекту можно применять уже знакомые нам агрегирующие методы
# (mean, median, sum и т. д.), чтобы рассчитывать показатели внутри каждой группы.

# Мы получили таблицу,
# на пересечении строк и столбцов которой находятся
# средние значения каждого числового признака в наших данных.
melb_df.groupby('Type').mean()

# агрегирующие методы можно применять только к интересующему нас столбцу
melb_df.groupby('Type')['Price'].mean()

# найдём минимальное значение расстояния от центра города до объекта
# в зависимости от его региона. Результат отсортируем по убыванию расстояния:
melb_df.groupby('Regionname')['Distance'].min().sort_values(ascending=False)


# 10
# Чтобы рассчитать несколько агрегирующих методов,
# можно воспользоваться методом agg(),
# который принимает список строк с названиями агрегаций.
melb_df.groupby('MonthSale')['Price'].agg(
    ['count', 'mean', 'max']).sort_values('count', ascending=False)
# В результате применения метода agg(),
# в который мы передали список с названиями интересующих нас агрегирующих функций,
# мы получаем DataFrame со столбцами count, mean и max,
# где для каждого месяца рассчитаны соответствующие параметры.
# Результат сортируем по столбцу count.

# 11
# Если вам нужна полная информация обо всех
# основных статистических характеристиках внутри каждой группы,
# вы можете воспользоваться методом agg(),
# передав в качестве его параметра строку 'describe':
melb_df.groupby('MonthSale')['Price'].agg('describe')

# 12
# После базовых математических функций наиболее частым агрегированием
# является подсчёт числа уникальных значений.
melb_df.groupby('Regionname')['SellerG'].agg(['nunique', set])

# 13
# Сгруппируйте данные по признаку количества комнат
# и найдите среднюю цену объектов недвижимости в каждой группе.
melb_df.groupby('Rooms')['Price'].mean().sort_values(ascending=False)

# 14
# Какой регион имеет наименьшее стандартное
# отклонение по географической широте (Lattitude)?
melb_df.groupby('Regionname')['Lattitude'].std().sort_values()

# 15
# Какая риелторская компания (SellerG) имеет наименьшую общую выручку
# за период с 1 мая по 1 сентября (включительно) 2017 года?
# Для ответа на этот вопрос рассчитайте сумму продаж (Price)
# каждой компании в заданный период.
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_df['Date']) & (melb_df['Date'] <= date2)
melb_df[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True)

# 16
# Сводная таблица принимает на вход данные из отдельных столбцов и группирует их. 
# В результате получается новая таблица, которая позволяет увидеть многомерное обобщение 
# данных. Таким образом, благодаря сводным таблицам мы можем оценить зависимость 
# между двумя и более признаками данных.

if __name__ == '__main__':
    # 1
    print(quarters.value_counts().iloc[1])

    # 2
    print(melb_df.info())

    # 3
    print(melb_df.sort_values(by='Price').head(10))

    # 4
    print(melb_df.sort_values(
        by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])

    # 7
    print(int(melb_df.sort_values(by='AreaRatio', ignore_index=True,
                                  ascending=False).loc[1558, 'BuildingArea']))

    # 8
    print(int(res))

    # 11
    print(melb_df.groupby('MonthSale')['Price'].agg('describe'))

    # 13
    print(melb_df.groupby('Rooms')[
          'Price'].mean().sort_values(ascending=False))

    # 14
    print(melb_df.groupby('Regionname')['Lattitude'].std().sort_values())

    # 15
    print(melb_df[mask].groupby('SellerG')[
          'Price'].sum().sort_values(ascending=True))
