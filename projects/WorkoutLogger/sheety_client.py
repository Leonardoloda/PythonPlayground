from datetime import datetime

from requests import post, get


class SheetyClient:
    URL = "https://api.sheety.co/d7c73a0a228fcfcbb405d430492cc56f/workout/workouts"

    def __init__(self, token: str):
        self._token = token

    def add_workout(self, exercise: str, duration: str, calories: str):
        now = datetime.now()

        body = {
            "workout": {
                "date": now.strftime("%Y/%m/%d"),
                "time": now.strftime("%H:%M:%S"),
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._token}"
        }

        response = post(self.URL, json=body, headers=headers)

        response.raise_for_status()

        return response.json()

    def get_rows(self):
        response = get(self.URL)

        return response.json()
