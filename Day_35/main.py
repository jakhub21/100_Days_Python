import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 53.459499
MY_LONG = 14.452760

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remeber to bring an ☔️",
        from_=NUMBER,
        to="4634888768"
    )

    print(message.status)
