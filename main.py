import requests

API_URL = "https://www.themealdb.com/api/json/v1/1/filter.php"

response = requests.get(
    API_URL,
    params={"c": "Seafood"}, 
    timeout=10
    )

data = response.json()
print(data)
response.raise_for_status()