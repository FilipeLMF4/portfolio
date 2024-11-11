import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

WEIGHT = 81
HEIGHT = 181
AGE = 28

NUTRIX_HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

SHEETY_HEADER = {
    "Authorization": "Bearer token"
}

nutrix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/165a242f0a4568d9bcf7ccb27dacea11/100DaysCodeDay38MyWorkouts/workouts"


def get_calories_data():
    nutrix_params = {
        "query": input("What did you do today? "),
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
    }

    response = requests.post(url=nutrix_endpoint, json=nutrix_params, headers=NUTRIX_HEADER)
    return response.json()["exercises"]


def post_results(exercise_data):
    for exercise in exercise_data:
        name = exercise["name"]
        duration = exercise["duration_min"]
        calories = exercise["nf_calories"]

        sheety_params = {
            "workout": {
                "date": datetime.now().strftime("%x"),
                "time": datetime.now().strftime("%X"),
                "exercise": name.title(),
                "duration": round(duration, 1),
                "calories": round(calories, 0),
            }
        }

        sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=SHEETY_HEADER)
        print(sheety_response)


data = get_calories_data()
post_results(data)
