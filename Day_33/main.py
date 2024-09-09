import requests
from datetime import datetime
import smtplib
import os


MY_LAT = 53.459499
MY_LONG = 14.452760


my_email = os.environ.get('STMPLIB_EMAIL')
password = os.environ.get('STMPLIB_PASSWORD')

#ISS
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True


#SUN
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jakhub21@gmail.com",
                            msg=f"Subject:Look Up\n\nThe ISS is above you in the sky")