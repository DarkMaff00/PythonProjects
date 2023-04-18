import requests
import datetime as dt

# Your Api Key from Tequila
API_KEY = ""

header = {
    "apikey": API_KEY
}


class FlightSearch:
    def __init__(self):
        self.your_code = "KRK"
        self.tomorrow = dt.datetime.today() + dt.timedelta(1)
        self.six_months = dt.datetime.today() + dt.timedelta(6 * 30)
        self.currency = "PLN"

    def iata_code(self, city: str):
        params = {
            "term": city
        }
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=params, headers=header)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def search_for_price(self, destination_code):
        params = {
            "fly_from": self.your_code,
            "fly_to": destination_code,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.six_months.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "curr": self.currency,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
        }
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=params, headers=header)
        response.raise_for_status()
        data = response.json()['data'][0]
        return data
