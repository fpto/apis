import json
import requests
import pandas as pd

pd.options.display.max_columns = 20 # Default is only 60

api_token = '5eyBnve8x5pMbQ2bqqePKgMQAbfhwmszatuXBR5z'
public_key = 8801
api_url_base = 'https://api.loandisk.org/'
branch_id = 10573


headers = {'Content-Type': 'application/json','Authorization': 'Basic {0}'.format(api_token)}

destination_folder = 'dataset/'

#TODO: Function to get borrower_id from borrower_unique_number

def get_borrower_info(borrower_id):

    api_url = '{}{}/{}/loan/{}'.format(api_url_base, public_key,branch_id, borrower_id)
    #api_url = '{}{}/{}/borrower/from/1/count/100'.format(api_url_base, public_key,branch_id)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def list_loans(from_page,howmany):
    api_url = '{}{}/{}/loan/from/{}/count/{}'.format(api_url_base, public_key,branch_id,from_page,howmany)
    response = requests.get(api_url, headers=headers)
    print(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


# WHAT FUNCTION

#borrower_info = list_borrowers(0,186)
# Takes just the result of the query
#bd = borrower_info['response']['Results'][0]
#Creates a dataframe from it
#df = pd.DataFrame.from_dict(bd)

dfs = []

#TO DO
for x in range(102):
    # Only 50 seems to work
    loan_info = list_loans(x,51)
    # Takes just the result of the query
    bd = loan_info['response']['Results'][0]
    #Creates a dataframe from it
    df = pd.DataFrame.from_dict(bd)
    dfs.append(df)


todos_prestamos = pd.concat(dfs).reset_index()

#Print info
if loan_info is not None:
    print("Here's your info: ")
    #for k, v in bd.items():
    #    print('{0}:{1}'.format(k, v))
    # print(df[['borrower_id','borrower_unique_number','borrower_description']])
    print(todos_prestamos)

else:
    print('[!] Request Failed')


todos_prestamos.to_excel('madres_prestamos_2019_10_28.xlsx', index=False, sheet_name='prestamos')

#extra STUFF
