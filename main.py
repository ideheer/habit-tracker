import requests
from datetime import datetime

USERNAME = "ideheer"
TOKEN = "letusgothenuandI"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"commits",
    "type":"int",
    "color":"ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()

add_pixel = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many commits did you submit today? "),
}
response = requests.post(url=add_pixel_endpoint, json=add_pixel, headers=headers)
print(response.text)

# update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
#
# response = requests.put(url=update_graph_endpoint, json={"timezone":"Brazil/East"}, headers=headers)
# print(response.text)