import json
import requests
import pandas as pd
from get_bo_info import get_borrower_info
pd.options.display.max_columns = 20 # Default is only 60

api_token = '5eyBnve8x5pMbQ2bqqePKgMQAbfhwmszatuXBR5z'
public_key = 8801
api_url_base = 'https://api.loandisk.org/'
branch_id = 10573


headers = {'Content-Type': 'application/json','Authorization': 'Basic {0}'.format(api_token)}

# THIS IS TO UPDATE ONE SINGLE BORROWER
def update_borrower(borrower_id):
    #first load current infromation
    borrower_info = get_borrower_info(borrower_id)
    data = borrower_info['response']['Results'][0]
    #Modify only fields that you want to change
    data['borrower_description'] = 'AGAIN AGAIN THIS IS ME TESTING STUFF'
    #Build api url
    api_url = '{}{}/{}/borrower/'.format(api_url_base, public_key,branch_id)
    #Do the request
    response = requests.put(api_url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None




#response = update_borrower(914004)
