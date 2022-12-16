import pandas as pd
def load_data_frame():
    pd.set_option('display.max_rows', None)
    dataFrame = pd.read_csv('data/molecule_data.csv')
    dataFrame['dH'] = dataFrame['dH'].astype(float)
    return dataFrame
