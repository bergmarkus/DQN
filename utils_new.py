import numpy as np
import pandas as pd
import os
import glob

def get_data(folder, asset, start_date, end_date, cols=[1,4]):
    path = os.path.join(folder, asset + '.csv')
    df = pd.read_csv(path, index_col=0, usecols=cols, dtype=np.float32, parse_dates=True)
    df = df.iloc[::-1]
    df = df.loc[start_date:end_date]
    df.interpolate(method='linear', axis=0, inplace=True)
    
    return df

def get_data_list(folder, start_date, end_date, assets=None, cols=[1,4]):
    if assets == None:
        assets = [os.path.splitext(os.path.basename(x))[0] for x in glob.glob(folder + '*csv')]
    data = []
    for asset in assets:
        data.append(get_data(folder, asset, start_date, end_date, cols))

    df = pd.concat(data, axis=1, join='inner')
    
    return df