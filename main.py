import requests
import json

API_URL = "https://www.themealdb.com/api/json/v1/1/filter.php"
API_URL_ID = "https://www.themealdb.com/api/json/v1/1/lookup.php"
API_URL_LIST = "https://www.themealdb.com/api/json/v1/1/list.php"


def recipe_by_country(country):
    response = requests.get(API_URL, params={"a": country}, timeout=10)
    data = response.json()
    meals = data.get("meals")

    for meal in meals:
        print(meal["strmeal"], meal["idmeal"])

def recipe_by_category(category):
    response = requests.get(API_URL, params={"c": category}, timeout=10)
    data = response.json()
    meals = data.get("meals")
    
    for meal in meals:
        print(meal["strmeal"], meal["idmeal"])

def recipe_by_ingredient(ingredient):
    response = requests.get(API_URL, params={"i": ingredient}, timeout=10)
    data = response.json()
    meals = data.get("meals")

    for meal in meals:
        print(meal["idMeal"], meal["strMeal"])

def recipe_by_id(meal_id):
    response = requests.get(API_URL_ID, params={"i": meal_id}, timeout=10)
    data = response.json()
    meal = data.get("meals")[0]

    print(meal.keys())
    for number in range(1, 21):
        ingredient = meal.get(f"strIngredient{number}")
        measure = meal.get(f"strMeasure{number}")
        if ingredient and measure:
            print(f"{ingredient}: {measure}")
    print(meal["strInstructions"])
    print(meal["strYoutube"])
    print(meal["strSource"])

def view_categories():
    response = requests.get(API_URL_LIST, params={"i": "list"}, timeout=10)
    data = response.json()
    ingredients = data.get("meals")

    for ingredient in ingredients:
        print(ingredient["strIngredient"])
    with open("ingredients.json", "w") as file:
        json.dump([ingredient["strIngredient"] for ingredient in ingredients], file, indent=4)

def main():
    finished = False
    ingredients = []
    print("input ingredient or '1' ")

    while finished == False:
        user_input = input()
        if user_input == "1":
            finished = True
            print("Your ingredients are:", *ingredients)
        else:
            ingredients.append(user_input)

    recipe_by_ingredient(ingredients[0])
    
view_categories()
#main()