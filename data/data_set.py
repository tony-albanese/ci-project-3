import pandas as pd
def load_data_frame():
    dataFrame = pd.read_csv('molecule_data - data.csv')
    dataFrame['dH'] = dataFrame['dH'].astype(float)
    return dataFrame