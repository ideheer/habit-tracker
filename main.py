import requests
from datetime import datetime

pixela_username = os.environ["USERNAME"]
pixela_graphid = os.environ["GRAPHID"]
pixela_token = os.environ['TOKEN']
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"commits",
    "type":"int",
    "color":"ichou",
}

headers = {
    "X-USER-TOKEN": pixela_token
}
add_pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{pixela_graphid}"

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