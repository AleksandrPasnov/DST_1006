from calendar import weekday
import pandas as pd

melb_data = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_11_Работа с Pandas/data_csv/melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()

melb_df.to_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_11_Работа с Pandas/data_csv/melb_df.csv')
# print(melb_data.head)
# print()

melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
# melb_df.drop(['index','Coordinates'],axis=1,inplace=True) алтернативный вариант

# print(melb_df.head())
# print()

total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomSquare'] = melb_df['BuildingArea']/total_rooms

diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area

price_square = melb_df['Price'] ** 2
# print(price_square)

diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
# print(melb_df['AreaRatio'])

melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
# print(melb_df['Date'])


melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
# print(melb_df['AgeBuilding'])

melb_df = melb_df.drop('YearBuilt', axis=1)

melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5)
                        | (melb_df['WeekdaySale'] == 6)]
# print(weekend_count.shape)
# print(melb_df['Address'].nunique())


def get_street_type(address):
    # Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
# Метод split() разбивает строку на слова по пробелу.
# В результате получаем список слов в строке и заносим его в переменную address_list.
    address_list = address.split(' ')
# Обрезаем список, оставляя в нём только последний элемент,
# потенциальный подтип улицы, и заносим в переменную street_type.
    street_type = address_list[-1]
# Делаем проверку на то, что полученный подтип является географической пометкой.
# Для этого проверяем его на наличие в списке exclude_list.
    if street_type in exclude_list:
        # Если переменная street_type является географической пометкой,
        # переопределяем её на второй элемент с конца списка address_list.
        street_type = address_list[-2]
# Возвращаем переменную street_type, в которой хранится подтип улицы.
    return street_type


street_types = melb_df['Address'].apply(get_street_type)
"""функция пишется для одного элемента столбца, 
   а метод apply() применяется к каждому его элементу
    """
# print(street_types)
popular_stypes = street_types.value_counts().nlargest(10).index
melb_df['StreetType'] = street_types.apply(
    lambda x: x if x in popular_stypes else 'other')
# print(melb_df['StreetType'])

melb_df = melb_df.drop('Address', axis=1)


def get_weeknd(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else:
        return 0


melb_df['WeekdaySale'] = melb_df['WeekdaySale'].apply(get_weeknd)

mask_1 = melb_df['WeekdaySale'] == 1

# print(round(melb_df[mask_1]['Price'].mean(), 2))

popular_seller = melb_df['SellerG'].value_counts().nlargest(49).index

melb_df['SellerG'] = melb_df['SellerG'].apply(
    lambda x: x if x in popular_seller else 'other')

# список столбцов, которые мы не берём во внимание
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
# задаем максимальное число уникальных категорий
max_unique_count = 150
#  цикл по менам столбцов
for col in melb_df.columns:
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude:
        melb_df[col] = melb_df[col].astype('category')

popular_Suburb = melb_df['Suburb'].value_counts().nlargest(119).index

melb_df['Suburb'] = melb_df['Suburb'].apply(
    lambda x: x if x in popular_Suburb else 'other'
)

data = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_11_Работа с Pandas/data_csv/citibike-tripdata.csv', sep=',')

# print(data['start station id'].value_counts())
# print(data['bikeid'].mode()[0])

mode_usertype = data['usertype'].mode()[0]
count_mode_user = data[data['usertype'] == mode_usertype].shape[0]
# print(round(count_mode_user / data.shape[0], 2))

male_count = data[data['gender'] == 1].shape[0]
female_count = data[data['gender'] == 0].shape[0]
# print(max([male_count, female_count]))

data['starttime'] = pd.to_datetime(data['starttime'])
data['stoptime'] = pd.to_datetime(data['stoptime'])
data['trip duration'] = (data['stoptime'] - data['starttime'])
print(data.loc[3, 'trip duration'])

weekday = data['starttime'].dt.dayofweek
data['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
print(data['weekend'].sum())

def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'
data['time_of_day'] = data['starttime'].dt.hour.apply(get_time_of_day)
a = data[data['time_of_day'] == 'day'].shape[0]
b = data[data['time_of_day'] == 'night'].shape[0]
print(round(a / b))