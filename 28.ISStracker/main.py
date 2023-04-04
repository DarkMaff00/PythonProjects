import time
import requests
import datetime as dt
import smtplib

# Find it at https://www.latlong.net
# Your latitude
MY_LAT = 50.071683
# Your longitude
MY_LNG = 19.941466

# Your email
MY_EMAIL = ""
# Generate App password in your mailbox
PASSWORD = ""

# Receiver email
RECEIVER = ""


def is_iss_overhead():
    # http://open-notify.org/Open-Notify-API/ISS-Location-Now/
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    lat = float(data['iss_position']['latitude'])
    lng = float(data['iss_position']['longitude'])
    if MY_LAT - 5 < lat < MY_LAT + 5 and MY_LNG - 5 < lng < MY_LNG + 5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }

    #   https://sunrise-sunset.org
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if sunset <= time_now or time_now <= sunrise:
        return True


while True:
    if is_iss_overhead() and is_night():
        # Change "smtp.gmail.com" depending on your mailbox [search for this in Internet]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                                msg=f"Subject:ISS Overhead\n\nLook Up there is ISS over your head. Enjoy the view ")
    time.sleep(60)
