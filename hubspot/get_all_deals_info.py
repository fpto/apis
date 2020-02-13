import json
import requests
import pandas as pd
from hubspot3 import Hubspot3

pd.options.display.max_columns = 20 # Default is only 60

API_KEY = 'fda2dd05-e3cc-4ce2-93be-133139408283'
client = Hubspot3(api_key=API_KEY)

# Select all contacts
all_deals = client.deals.get_all()
all_deals = pd.DataFrame.from_dict(all_deals)

print(all_deals.head())
