import pandas as pd

melb_data = pd.read_csv(
    '/Users/MacBook/Desktop/Data Saintist/IDE/PY_11_Работа с Pandas/data_csv/melb_data_ps.csv', sep=',')

melb_df = melb_data()

if __name__ == '__main__':
    print(melb_data.head)
