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


#load test dataframe
#To deal with leading zeros
#dtype_dic = {'borrower_unique_number':str,'custom_field_3528':str}

test_dataframe = pd.read_excel("pagos_test.xlsx", sheet_name="prestamos")
#working_dataframe = pd.read_excel("madres_2019_10_24-corregir-codigo-contable.xlsx", sheet_name="participantes", dtype = dtype_dic)

#TODO Create a function that takes a dataframe with an additional column and updates value


def update_each_repayment(dataframe,new_column):
    #first load current infromation
    print("Updating the column: " + new_column)

    for index, row in dataframe.iterrows():
        repayment_id = row['repayment_id']
        print("Updating for repayment_id: " + str(repayment_id))
        #first load current infromation
        borrower_info = get_payment_info(repayment_id)
        data = borrower_info['response']['Results'][0]
        print(new_column + " was: " + str(data[new_column]))
        data[new_column] = row[new_column]
        print(new_column + " is now: " + str(row[new_column]))
        #Build api url
        api_url = '{}{}/{}/repayment/'.format(api_url_base, public_key,branch_id)
        print(api_url)
        #Do the request
        response = requests.put(api_url, data=json.dumps(data), headers=headers)
        #if response.status_code == 200:
        #    return json.loads(response.content.decode('utf-8'))
        #else:
        #    return None



update_each_repayment(test_dataframe,'repayment_adjust_remaining_schedule')
