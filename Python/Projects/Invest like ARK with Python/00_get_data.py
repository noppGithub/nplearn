from pathlib import Path
import requests
import datetime
import os

def create_folder(path):
    """
    create folder according to the input path
    """
    p = Path(path)
    p.mkdir(parents=True,exist_ok=True)

def get_data(url):
    response = requests.get(url,stream=True)
    return response.text

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

now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
path_name = f"./data/{now_time}"
create_folder(path_name)

for fund_name,url in funds.items():
    data = get_data(url)
    file_name = f"{fund_name}.csv"
    file_path = os.path.join(path_name,file_name)
    with open(file_path,'w') as file:
        file.write(data)
