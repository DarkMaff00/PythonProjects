import requests
from datetime import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = ''
TOKEN = ''

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Creating User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': 'graph1',
    'name': 'Hydration Tracking',
    'unit': 'L',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN,
}

# Creating graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = dt.now()

pixel_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input("How much water did you drink today? "),
}

# Adding activity to our graph
response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
update_data = {
    'quantity': '1.2',
}

# Updating activity in our graph
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# Deleting activity in our graph
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
