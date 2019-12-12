import json
import requests
import pandas as pd

pd.options.display.max_columns = 20 # Default is only 60

api_token = '5eyBnve8x5pMbQ2bqqePKgMQAbfhwmszatuXBR5z'
public_key = 8801
api_url_base = 'https://api.loandisk.org/'
branch_id = 10573

########
repayment_id = 914004

headers = {'Content-Type': 'application/json','Authorization': 'Basic {0}'.format(api_token)}

destination_folder = 'dataset/'

#TODO: Function to get borrower_id from borrower_unique_number

def get_payment_info(repayment_id):

    api_url = '{}{}/{}/repayment/{}'.format(api_url_base, public_key,branch_id, repayment_id)
    #api_url = '{}{}/{}/borrower/from/1/count/100'.format(api_url_base, public_key,branch_id)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
