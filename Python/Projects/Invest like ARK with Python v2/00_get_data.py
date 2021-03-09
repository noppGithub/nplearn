from pathlib import Path
import requests
import datetime
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from shutil import copy2

# ETF urls
funds = {
    'ARKK INNOVATION ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv',
    'ARKQ Autonomous Technology & Robotics ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv',
    'ARKW Next Generation Internet ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv',
    'ARKG Genomic Revolution ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv',
    'ARKF FINTECH INNOVATION ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv',
    'PRNT The 3D Printing ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv',
    'IZRL Israel Innovative Technology ETF':'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv'
}

# ====================================== Functions ======================================
def create_folder(path):
    """
    create folder according to the input path
    """
    p = Path(path)
    p.mkdir(parents=True,exist_ok=True)

def get_data(url):
    response = requests.get(url,stream=True)
    return response.text

def read_latest_data():
    mypath = './data'
    paths = [p for p in listdir(mypath) if not isfile(join(mypath, p))]
    paths.sort()
    path = paths[-1]
    mypath = join(mypath,path)
    files = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]
    dfs = []
    for f in files:
        dfs.append(pd.read_csv(f))
    df = pd.concat(dfs)
    # format and filter
    df = df[df['fund'].notna()]
    df = df[df['ticker'].notna()]
    df['date'] = pd.to_datetime(df['date'],format="%m/%d/%Y")
    df['insert_date'] = pd.Timestamp.now()
    return df

def download_data():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    path_name = f"./data/{now_time}"
    create_folder(path_name)
    for fund_name,url in funds.items():
        data = get_data(url)
        file_name = f"{fund_name}.csv"
        file_path = os.path.join(path_name,file_name)
        with open(file_path,'w') as file:
            file.write(data)

def create_or_update_master():
    # create current data if not exist
    file_current = './master.csv'
    df = read_latest_data()
    if os.path.exists(file_current):
        # create backup so you can go back if something is wrong 
        # and update the current file
        copy2(file_current,'./_backup_master.csv')
        # append data
        df_current = pd.read_csv(file_current)
        df = pd.concat([df_current,df])
    df.to_csv(file_current,index=False,encoding='utf-8')
    
# df[df['ticker']=='TSLA']
# ====================================== Application ======================================
download_data()
create_or_update_master()