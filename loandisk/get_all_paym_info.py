import json
import requests
import pandas as pd
from get_paym_info import get_payment_info

pd.options.display.max_columns = 20 # Default is only 60

api_token = '5eyBnve8x5pMbQ2bqqePKgMQAbfhwmszatuXBR5z'
public_key = 8801
api_url_base = 'https://api.loandisk.org/'
branch_id = 10573


headers = {'Content-Type': 'application/json','Authorization': 'Basic {0}'.format(api_token)}

destination_folder = 'dataset/'


#TODO: Function to get borrower_id from borrower_unique_number


def list_repayments(from_page,howmany):
    api_url = '{}{}/{}/repayment/from/{}/count/{}'.format(api_url_base, public_key,branch_id,from_page,howmany)
    response = requests.get(api_url, headers=headers)
    print(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

dfs = []

#TO DO
for x in range(6):
    # Only 50 seems to work
    loan_info = list_repayments(x,51)
    # Takes just the result of the query
    bd = loan_info['response']['Results'][0]
    #Creates a dataframe from it
    df = pd.DataFrame.from_dict(bd)
    dfs.append(df)


todos_pagos = pd.concat(dfs).reset_index()

#Print info
if loan_info is not None:
    print("Here's your info: ")
    #for k, v in bd.items():
    #    print('{0}:{1}'.format(k, v))
    # print(df[['borrower_id','borrower_unique_number','borrower_description']])
    print(todos_pagos)

else:
    print('[!] Request Failed')


todos_pagos.to_excel('pagos_madres_prestamos_2020_2_13_con_devs18.xlsx', index=False, sheet_name='prestamos')
