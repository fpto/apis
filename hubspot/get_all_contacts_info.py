import json
import requests
import pandas as pd
from hubspot3 importHubspot3

pd.options.display.max_columns = 20 # Default is only 60

API_KEY = 'fda2dd05-e3cc-4ce2-93be-133139408283'
client = Hubspot3(api_key=API_KEY)

# Select all contacts
all_contacts = client.contacts.get_all()
all_contacts = pd.DataFrame.from_dict(all_contacts)
