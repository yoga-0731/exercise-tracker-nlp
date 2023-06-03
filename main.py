import requests
import os
from datetime import datetime

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
parameters = {
    "query": input("Tell me what you did today? : "),
    "gender": "female"
}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=parameters)
exercise_data = response.json()


sheet_endpoint = os.environ.get('SHEETY_ENDPOINT')
now = datetime.now()
headers = {"Authorization": os.environ.get('BEARER_TOKEN')}
for exercise in exercise_data['exercises']:
    sheet_parameters = {
        "sheet1": {
            "date": str(now.strftime('%d/%m/%Y')),
            "time": str(now.time().strftime('%H:%M:%S')),
            "exercise": exercise['user_input'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    response = requests.post(url=sheet_endpoint, headers=headers, json=sheet_parameters)

