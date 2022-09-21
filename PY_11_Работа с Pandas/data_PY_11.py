import pandas as pd

melb_data = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_11_Работа с Pandas/data_csv/melb_data_ps.csv', sep=',')

melb_df = melb_data.copy()
# print(melb_data.head)
# print()

melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
# melb_df.drop(['index','Coordinates'],axis=1,inplace=True) алтернативный вариант

# print(melb_df.head())
# print()

total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomSquare'] = melb_df['BuildingArea']/total_rooms

price_square = melb_df['Price'] **2
print(price_square)