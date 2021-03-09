import pandas as pd
from os import listdir
from os.path import isfile,join,split

# old data
file_path = './data/2021-02-06_01-29-22'
files = [join(file_path,file) for file in listdir(file_path) if isfile(join(file_path,file))]
dfs =[]
for file in files:
    dfs.append(pd.read_csv(file))
df_old = pd.concat(dfs)
df_old = df_old[df_old['fund'].notna()]
df_old = df_old[df_old['ticker'].notna()]
df_old = df_old[['fund','ticker','shares']]
df_old.columns = ['fund','ticker','shares_old']

# new data
file_path = './data/2021-02-06_01-30-02'
files = [join(file_path,file) for file in listdir(file_path) if isfile(join(file_path,file))]
dfs =[]
for file in files:
    dfs.append(pd.read_csv(file))
df_new = pd.concat(dfs)
df_new = df_new[df_new['fund'].notna()]
df_new = df_new[df_new['ticker'].notna()]
df_new = df_new[['fund','ticker','shares']]
df_new.columns = ['fund','ticker','shares_new']

# compare them
df = df_old.merge(df_new,on=['fund','ticker'],how='outer')
df.fillna(0,inplace=True)
df['diff'] = df['shares_new'] - df['shares_old']

print(df[df['diff'] != 0])

df[df['diff'] != 0].to_csv('./diff.csv',index=False)