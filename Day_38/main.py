import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 180
AGE = 23

APP_ID = os.environ.get('NUTRITION_APP_ID')
API_KEY = os.environ.get('NUTRITION_API_KEY')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

GOOGLE_SHEET_NAME = "workout"
sheety_endpont  = "https://api.sheety.co/45edf4df9f607f4d3221c3020917c36e/workoutTracking/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        sheety_endpont,
        json=sheet_input,
        auth=(
            "jakhub21@gmail.com",
            os.environ.get("SHEETY_PASSWORD")
        )
    )

    print(f"Sheety Response: \n {sheet_response.text}")

