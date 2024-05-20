import requests
import streamlit as st

st.set_page_config(page_title="FDA API Feeds, check out device data feeds from the Food and Drug Administration", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("FDA Data")

"""
This request structure pulls down JSON from the API into a Python readable request format using the built-in request dunder module. The Sample uses FDA device model data
"""

url = "https://api.fda.gov/device/event.json?search=date_received:[20230101+TO+20241231]&limit=5"

payload = {}
headers = {
  'Authorization':'Gyw2G5ZHScnftGXZxopdCwaM3R2fZYq5B96P9ZNK',
  'Api-Version': '<json>',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print the request, you can also import a web assembly module using python flask or my personal fav streamlit st functions
st.json(response)

