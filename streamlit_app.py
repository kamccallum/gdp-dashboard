import streamlit as st
import pandas as pd
import math
import requests
import json
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Olympics dashboard',
    page_icon=':tennis:', # This is an emoji shortcode. Could be a URL too.
)

#grab Olympics point submissions
api_key = 'sk_prod_jdzrsSN1iDS7X1nPqDKdIPqhUM1baZWa17uT7pMq4g9erNbHrkNNtyoWmByQxDLwVYUwDeBPqlb4BLpqizr78qXMYh0flpof3h3_27197'
form_id = 'vsGn68PP3Fus'

# Construct the API endpoint URL
url = f'https://api.fillout.com/v1/api/forms/{form_id}/submissions'

# Set up the headers with your API key
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
all_responses = []
offset = 0
limit = 150  # max allowed

while True:
    params = {'offset': offset, 'limit': limit}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    responses = data.get('responses', [])
    all_responses.extend(responses)

    print(f"Fetched {len(responses)} responses at offset {offset}")

    # if fewer than limit were returned, we've reached the end
    if len(responses) < limit:
        break
    offset += limit

print(f"✅ All responses fetched — total records: {len(all_responses)}")

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :tennis: Olympics dashboard

'''

# Add some spacing
''
''


