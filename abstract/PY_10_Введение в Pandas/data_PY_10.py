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

# countries_df = pd.DataFrame(
#     data= [
#         ['England', 56.29, 133396],
#         ['Canada', 38.05, 9984670],
#         ['USA', 322.28, 9826630],
#         ['Russia', 146.24, 17125191],
#         ['Ukraina', 45.5, 603628],
#         ['Belarus', 9.5, 207600],
#         ['Kazahstan', 17.04, 2724902]
#     ],
#     columns= ['country', 'population', 'square'],
#     index= ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
# )

# countries_df.to_csv('/Users/MacBook/Desktop/Data Saintist/IDE/abstract/PY_10_Введение в Pandas/data_csv/countries.csv', index=False, sep=';')
# # print(countries_df.mean(axis=0))
# # print()
# # print(countries_df.population)
# # print()
# # print(countries_df['population'])
# # print()
# # print(countries_df.loc['RU', ['population', 'square']])
# # print(countries_df.loc[['UA', 'BY', 'KZ'],['population', 'square']])

# # incomes = [478, 512, 196]
# # expenses = [156, 130, 270]
# # years = [2018, 2019, 2020]

# # def create_companyDF(incomes, expenses, years):
# #     df= pd.DataFrame ({
# #         'Incomes': incomes,
# #         'Expenses': expenses
# #         },
# #         index= years
# #     )
# #     return df

# # def get_profit(df, year):
# #     if year in df.index:
# #         profit = df.loc[year, 'Incomes'] - df.loc[year, "Expenses"]
# #     else:
# #         profit = None
# #     return profit

# # if __name__ == '__main__':
        
# #     scienceyou = create_companyDF(incomes, expenses, years)
# #     print(get_profit(scienceyou, 2020)) #-74

data = pd.read_csv('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv')
print(data)