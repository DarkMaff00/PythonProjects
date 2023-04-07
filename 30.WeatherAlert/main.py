import requests
from twilio.rest import Client

# Your private Api key from OpenWeatherMap.org
API_KEY = ""
# Find it at https://www.latlong.net
LATITUDE = 50.071683
LONGITUDE = 19.941466

# Twilio SID Account and Authorization Token
account_sid = ''
auth_token = ''


parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()['hourly']
hourly_weather = data[:12]
for hour in hourly_weather:
    if hour['weather'][0]['id'] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella.",
            # Your trial number from Twilio
            from_="",
            # Your verified number from Twilio
            to=""
        )
        print(message.status)
        break

