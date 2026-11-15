import requests

API_URL = "https://www.themealdb.com/api/json/v1/1/filter.php"
API_URL_ID = "https://www.themealdb.com/api/json/v1/1/lookup.php"

def recipe_by_country(country):
    response = requests.get(API_URL, params={"a": country}, timeout=10)
    data = response.json()
    meals = data.get("meals")

    for meal in meals:
        print(meal["strMeal"], meal["idMeal"])

def recipe_by_category(category):
    response = requests.get(API_URL, params={"c": category}, timeout=10)
    data = response.json()
    meals = data.get("meals")
    
    for meal in meals:
        print(meal["strMeal"], meal["idMeal"])

def recipe_by_id(meal_id):
    response = requests.get(API_URL_ID, params={"i": meal_id}, timeout=10)
    data = response.json()
    meal = data.get("meals")[0]

    for number in range(1, 21):
        ingredient = meal.get(f"strIngredient{number}")
        measure = meal.get(f"strMeasure{number}")
        if ingredient and measure:
            print(f"{ingredient}: {measure}")

recipe_by_country("Canadian")
recipe_by_id("52928")