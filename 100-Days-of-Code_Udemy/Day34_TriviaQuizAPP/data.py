import requests

NR_QUESTIONS = 10
TYPE = "boolean"

parameters = {
    "amount": NR_QUESTIONS,
    "type": TYPE,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
