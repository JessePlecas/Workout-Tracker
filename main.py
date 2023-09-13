import requests
import time
from datetime import datetime
import os

now = datetime.now()

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]


workout_input = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

body_params = {
    "query": workout_input,
    "gender": "female",
    "weight_kg": 60,
    "height_cm": 173,
    "age": 36
}

response = requests.post(url=nutrition_endpoint, json=body_params, headers=headers)
result = response.json()

today = now.strftime("%Y%m%d")
time_now = time.strftime("%H:%M:%S", time.localtime())

bearer_headers = {
    "Authorization": "Bearer hoXft60Jtrf#Jga182"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    data = sheet_response.json()