from datetime import datetime
from os import getenv

from dotenv import load_dotenv

from nutritionix_client import NutritionixClient
from sheety_client import SheetyClient

load_dotenv()

API_KEY = getenv('API_KEY')
APP_ID = getenv('APP_ID')
SHEETY_TOKEN = getenv('SHEETY_TOKEN')

exercise_client = NutritionixClient(api_key=API_KEY, app_id=APP_ID)
sheety_client = SheetyClient(token=SHEETY_TOKEN)

now = datetime.now()

print("""
Welcome to Workout Logger
""")

workout = input("What did you do?\nAnswer: ")

exercise_response = exercise_client.parse_exercise(prompt=workout)
exercises = exercise_response["exercises"]

for exercise in exercises:
    sheety_client.add_workout(
        exercise=exercise["name"],
        duration=exercise["duration_min"],
        calories=exercise["nf_calories"]
    )

print(f"Added {len(exercises)} workouts to the drive")
