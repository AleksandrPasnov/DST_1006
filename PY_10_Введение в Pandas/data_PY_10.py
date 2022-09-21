import pandas as pd

countries = pd.Series(
    data = ['England', 'Canada', 'USA', 
            'Russia', 'Ukraina', 'Belarus', 'Kazahstan'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
    name = 'countries'
)
# print(countries)
# print()
# print(countries.loc['RU'])
# print()
# print(countries.loc[['US', 'RU', 'UK']])
# print()
# print(countries.iloc[4])
# print()
# print(countries.iloc[1:4])
# print()

names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]

def create_medications(names, count):
    """Функция создает объект Series
    Args:
        names (_string_): название лекарств
        count (_int_): их количество
    """
    res = pd.Series(data=counts, index=names)
    return res

medical = create_medications(names, counts)

def get_percent(medical, name):
    """Функция возвращает процент лекарства из списка

    Args:
        medical (_Series_): _объект Series_
        name (_str_): _название лекарства из списка_
    """
    return (medical.loc[name]/sum(medical) * 100)

# print(get_percent(medical, 'afobazol'))

coutries_df = pd.DataFrame({
    
    'country': ['England', 'Canada', 'USA', 'Russia', 
                'Ukraina', 'Belarus', 'Kazahstan'],
    'population': [56.29, 38.05, 322.28, 146.24, 
                   45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191,
               603628, 207600, 2724902]
})
coutries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
# print(coutries_df)

melb_data = pd.read_csv('/Users/MacBook/Desktop/Data Saintist/IDE/PY_10_Введение в Pandas/data_csv/melb_data.csv', sep=',')

# print(round(melb_data.loc[3521, 'Landsize'] / melb_data.loc[1690, 'Landsize']))

# Изменение типа данных в столбцах метод astype()
melb_data['Car'] = melb_data["Car"].astype('int64')

student_data = pd.read_csv('/Users/MacBook/Desktop/Data Saintist/IDE/PY_10_Введение в Pandas/data_csv/students_performance.csv', sep=',')   

# Часто при работе с таблицей нужно быстро посмотреть на основные статистические 
# свойства её столбцов. Для этого можно воспользоваться методом DataFrame describe().
# print(melb_data.describe())

if __name__ == "__main__":
    a = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
    b = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].mean()
    print(round(abs(a - b)))
#     print(melb_data.shape)
#     melb_data.info()
#     print(melb_data.describe())
    
