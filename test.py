import requests

# GET запрос с авторизацией
# url = 'http://127.0.0.1:8000/api/branches/'
# headers = {'Authorization': 'Phone 198765432'}
# response = requests.get(url, headers=headers)
# print(response.json())

# POST запрос
url = 'http://127.0.0.1:8000/api/visits/'
headers = {'Authorization': 'Phone 123456789', 'Content-Type': 'application/json'}
data = {
    'branch': 1,
    'latitude': 40.7128,
    'longitude': -74.0060
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
