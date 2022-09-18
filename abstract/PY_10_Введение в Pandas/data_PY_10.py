import pandas as pd

# countries = pd.Series(
#     data = ['England', 'Canada', 'USA', 
#             'Russia', 'Ukraina', 'Belarus', 'Kazahstan'],
#     index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
#     name = 'countries'
# )
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

# names=['chlorhexidine', 'cyntomycin', 'afobazol']
# counts=[15, 18, 7]

# def create_medications(names, count):
#     """Функция создает объект Series
#     Args:
#         names (_string_): название лекарств
#         count (_int_): их количество
#     """
#     res = pd.Series(data=counts, index=names)
#     return res

# medical = create_medications(names, counts)

# def get_percent(medical, name):
#     """Функция возвращает процент лекарства из списка

#     Args:
#         medical (_Series_): _объект Series_
#         name (_str_): _название лекарства из списка_
#     """
#     return (medical.loc[name]/sum(medical) * 100)

# print(get_percent(medical, 'afobazol'))

# coutries_df = pd.DataFrame({
    
#     'country': ['England', 'Canada', 'USA', 'Russia', 
#                 'Ukraina', 'Belarus', 'Kazahstan'],
#     'population': [56.29, 38.05, 322.28, 146.24, 
#                    45.5, 9.5, 17.04],
#     'square': [133396, 9984670, 9826630, 17125191,
#                603628, 207600, 2724902]
# })
# coutries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']

countries_df = pd.DataFrame(
    data= [
        ['England', 56.29, 133396],
        ['Canada', 38.05, 9984670],
        ['USA', 322.28, 9826630],
        ['Russia', 146.24, 17125191],
        ['Ukraina', 45.5, 603628],
        ['Belarus', 9.5, 207600],
        ['Kazahstan', 17.04, 2724902]
    ],
    columns= ['country', 'population', 'square'],
    index= ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
)
