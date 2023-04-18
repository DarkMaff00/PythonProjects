import requests

# Endpoints from Sheety
GET_ENDPOINT = ""
PUT_ENDPOINT = ""

# Your Bearer Token from Sheety
header = {
    "Authorization": "",
}


class DataManager:
    def __init__(self):
        response = requests.get(url=GET_ENDPOINT, headers=header)
        response.raise_for_status()
        self.prices = response.json()['prices']

    def updateData(self, updated_data):
        data = {
            'price': {
                'iataCode': updated_data['iataCode'],
            }
        }
        response = requests.put(url=f"{PUT_ENDPOINT}{updated_data['id']}", json=data, headers=header)
        response.raise_for_status()
