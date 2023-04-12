import requests
import datetime as dt
from twilio.rest import Client

# Twilio SID Account and Authorization Token
account_sid = ""
auth_token = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Your API keys
ALPHA_API_KEY = ""
NEWS_API_KEY = ""

stock_parameters = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK,
    'interval': '60min',
    'apikey': ALPHA_API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
stock_data = response.json()['Time Series (60min)']
yesterday = dt.date.today() - dt.timedelta(1)
yesterday_price = float(stock_data[f"{yesterday} 20:00:00"]['4. close'])
before_yesterday_price = float(stock_data[f"{yesterday - dt.timedelta(1)} 20:00:00"]['4. close'])
difference = abs(yesterday_price - before_yesterday_price)
diff_percent = (difference / yesterday_price) * 100

# If difference is greater than 5%, send SMS alert with most popular news about share creator
if diff_percent > 5:
    if yesterday_price > before_yesterday_price:
        emote = "🔺"
    else:
        emote = "🔻"
    news_parameters = {
        'q': COMPANY_NAME,
        'from': yesterday,
        'sortBy': 'popularity',
        'language': 'en',
        'apiKey': NEWS_API_KEY,
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    article = news_response.json()['articles'][0]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{STOCK}: {emote} {round(diff_percent)}%\n"
             f"Headline: {article['title']}\n"
             f"Brief: {article['description']}",
        # Your trial number from Twilio
        from_="",
        # Your verified number from Twilio
        to=""
    )
    print(message.status)
