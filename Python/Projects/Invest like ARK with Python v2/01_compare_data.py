import pandas as pd
from os import listdir
from os.path import isfile,join,split

# load data
df = pd.read_csv('./master.csv')
df['date'] = pd.to_datetime(df['date'],format="%Y-%m-%d")

# check that we have at least 2 dates
if df['insert_date'].nunique() > 1:
    # make compare
    dates = list(df['insert_date'].unique())
    old_date = dates[-2]
    new_date = dates[-1]
    df_old = df[df['insert_date']==old_date]
    df_new = df[df['insert_date']==new_date]
    # change column names
    df_old = df_old[['fund','ticker','shares']]
    df_old.columns = ['fund','ticker','shares_old']
    df_new = df_new[['fund','ticker','shares']]
    df_new.columns = ['fund','ticker','shares_new']
    # compare and output them
    df = df_old.merge(df_new,on=['fund','ticker'],how='outer')
    df.fillna(0,inplace=True)
    df['diff'] = df['shares_new'] - df['shares_old']
    df[df['diff'] != 0].to_csv('./diff.csv',index=False)
else:
    # add more data
    print('Please run 00_get_data.py to get updated data, now you have only 1 date to compare')

