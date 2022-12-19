import pandas as pd


def load_data_frame():
    pd.set_option('display.max_rows', None)
    data_frame = pd.read_csv('data/molecule_data.csv')
    data_frame['dH'] = data_frame['dH'].astype(float)
    return data_frame
