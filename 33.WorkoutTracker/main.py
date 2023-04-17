import requests
import datetime as dt

# Provide your API key and App ID from nutritionix
APP_ID = ""
API_KEY = ""

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

request_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 178,
    "age": 23,
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=request_params,
                         headers=headers)
response.raise_for_status()
data = response.json()['exercises'][0]

body = {
    'workout': {
        'date': dt.datetime.now().strftime('%d/%m/%Y'),
        'time': dt.datetime.now().strftime('%H:%M:%S'),
        'exercise': data['user_input'].title(),
        'duration': data['duration_min'],
        'calories': data['nf_calories'],
    }
}

# Provide Your Bearer Token from Sheety
header = {
    'Authorization': '',
}

# Provide generated POST endpoint to you google Sheet from Sheety
sheety_response = requests.post(url="",
                                json=body, headers=header)
sheety_response.raise_for_status()
