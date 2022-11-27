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

# 17
# На самом деле мы с вами уже строили простейшие одномерные сводные таблицы 
# с помощью метода groupby — мы рассматривали сводную таблицу в контексте группировки 
# по одному признаку. 
# Например, мы уже умеем строить таблицу, 
# которая показывает зависимость медианной цены и площади здания от числа комнат:

melb_df.groupby('Rooms')[['Price', 'BuildingArea']].median()

melb_df.groupby(['Rooms', 'Type'])['Price'].mean()

# 18
# Для того, чтобы финальный результат был представлен в виде сводной таблицы 
# (первый группировочный признак по строкам, а второй — по столбцам), 
# а не в виде Series с иерархическими индексами, 
# к результату чаще всего применяют метод unstack(), 
# который позволяет переопределить вложенный индекс в виде столбцов таблицы:

melb_df.groupby(['Rooms', 'Type'])['Price'].mean().unstack()

# 19
# На самом деле метод groupby редко используется при двух параметрах, 
# так как для построения сводных таблиц существует специальный 
# и более простой метод — pivot_table().

# Давайте построим ту же самую таблицу, 
# но уже с использованием метода pivot_table. 
# В качестве параметра values укажем столбец Price, 
# в качестве индексов сводной таблицы возьмём Rooms, а в качестве столбцов — Type. 
# Агрегирующую функцию оставим по умолчанию (среднее). 
# Дополнительно заменим пропуски в таблице на значение 0. 
# Финальный результат для наглядности вывода округлим с помощью метода round() до целых.

melb_df.pivot_table(
    values='Price',
    index='Rooms',
    columns='Type',
    fill_value=0
).round()

# 20

melb_df.pivot_table(
    values='Price',
    index='Regionname',
    columns='Weekend',
    aggfunc='count'
)

# 21

melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    aggfunc=['median', 'mean'],
    fill_value=0
)

# 22

melb_df.pivot_table(
    values='Price',
    index=['Method','Type'],
    columns='Regionname',
    aggfunc='median',
    fill_value=0
)

# 23 
# Объединение DataFrame: знакомимся с новыми данными (задание рейтинг фильмов)

ratings1 = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_12_Продвинутые методы Pandas/data_csv/ratings1.csv')

ratings2 = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_12_Продвинутые методы Pandas/data_csv/ratings2.csv')

dates = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_12_Продвинутые методы Pandas/data_csv/dates.csv')

ratings = pd.concat([ratings1, ratings2], ignore_index=True)

ratings = ratings.drop_duplicates(ignore_index=True)

ratings_dates = pd.concat([ratings, dates], axis=1)

# 24
# Для объединения двух таблиц по индексам используется метод DataFrame join(). 
# Однако данный метод можно применить и для того, 
# чтобы объединить таблицы по ключевому столбцу (в нашем случае это movieId).

movies = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_12_Продвинутые методы Pandas/data_csv/movies.csv')


joined_false = ratings_dates.join(
    movies,
    rsuffix='_right',
    how='left'
)

joined = ratings_dates.join(
    movies.set_index('movieId'),
    on='movieId',
    how='left'
)

# 25
# Аналогично предыдущему, метод merge() предназначен для слияния двух таблиц 
# по ключевым столбцам или по индексам. Однако, в отличие от join(), метод merge() 
# предлагает более гибкий способ управления объединением, 
# благодаря чему является более популярным.

merged = ratings_dates.merge(
    movies,
    on='movieId',
    how='left'
)

merged2 = ratings_dates.merge(
    movies,
    on='movieId',
    how='outer'
)

merge_ratings = ratings1.merge(ratings2, how='outer')

# 26

import re 
def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None

joined['year_release'] = joined['title'].apply(get_year_release)



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

    # 23
    print(ratings)
    print()
    print('Число строк в таблице ratings: ', ratings.shape[0])
    print('Число строк в таблице dates: ', dates.shape[0])
    print(ratings.shape[0] == dates.shape[0])
    print(ratings_dates.tail(7))
    
    # 24-25
    print(joined_false)
    
    print(joined.head())
    
    # 26
    print(joined.info())
    mask = joined['year_release'] == 1999
    print(joined[mask].groupby('title')['rating'].mean().sort_values())
    mask = joined['year_release'] == 2010
    print(joined[mask].groupby('genres')['rating'].mean().sort_values())
    print(joined.groupby('userId')['genres'].nunique().sort_values(ascending=False))
    print(joined.groupby('userId')['rating'].agg(
    ['count', 'mean']
).sort_values(['count', 'mean'], ascending=[True, False]))
