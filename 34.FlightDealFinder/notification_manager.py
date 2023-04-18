from twilio.rest import Client
from flight_data import FlightData

# Twilio SID Account and Authorization Token
ACCOUNT_SID = ''
AUTH_TOKEN = ''


class NotificationManager:

    def send_alert(self, information: FlightData):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f"Low price alert! Only PLN{information.price} to fly from "
                 f"{information.dep_city}-{information.dep_iata} to {information.dst_city}-{information.dst_iata}, "
                 f"from {information.outbound} to {information.inbound}.",
            # Your trial number from Twilio
            from_="",
            # Your verified number from Twilio
            to=""
        )
        print(message.status)
