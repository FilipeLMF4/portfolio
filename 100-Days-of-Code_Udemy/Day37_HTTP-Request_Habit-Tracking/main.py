import requests
from datetime import datetime

USERNAME = "user"
TOKEN = "token"
GRAPH_ID = "graph"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# # Create user
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

# # Create new graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Music Practice",
#     "unit": "minute",
#     "type": "int",
#     "color": "ajisai",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Post a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How long did you practice today (minutes)? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
