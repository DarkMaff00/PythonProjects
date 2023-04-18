from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.prices
flight_search = FlightSearch()

for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.iata_code(row['city'])
        data_manager.updateData(row)

for row in sheet_data:
    try:
        flight_data = flight_search.search_for_price(row['iataCode'])
    except IndexError:
        pass
    else:
        flight_represent = FlightData(flight_data)
        if flight_represent.price < row['lowestPrice']:
            notifier = NotificationManager()
            notifier.send_alert(flight_represent)
