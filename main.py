import requests
import json

URL = "https://www.themealdb.com/api/json/v1/1/filter.php"
ID_URL = "https://www.themealdb.com/api/json/v1/1/lookup.php"
LIST_URL = "https://www.themealdb.com/api/json/v1/1/list.php"

def fetch_recipe(category, search):
    # a = country, c = cuisine, i = ingredient
    response = requests.get(URL, params={category: search}, timeout=10)
    data = response.json()
    recipes = data.get("meals")

    for recipe in recipes:
        print(recipe["strmeal"], recipe["idmeal"])

def recipe_by_id(meal_id):
    response = requests.get(ID_URL, params={"i": meal_id}, timeout=10)
    data = response.json()
    recipe = data.get("meals")[0]

    print(recipe.keys())
    for number in range(1, 21):
        ingredient = recipe.get(f"strIngredient{number}")
        measure = recipe.get(f"strMeasure{number}")
        if ingredient and measure:
            print(f"{ingredient}: {measure}")
    print(recipe["strInstructions"])
    print(recipe["strYoutube"])
    print(recipe["strSource"])

def view_categories():
    response = requests.get(LIST_URL, params={"i": "list"}, timeout=10)
    data = response.json()
    ingredients = data.get("meals")

    for ingredient in ingredients:
        print(ingredient["strIngredient"])

    ingredient_dict = {
        index: item["strIngredient"]
        for index, item in enumerate(ingredients)
    }

    with open("ingredients.json", "w", encoding="utf-8") as file:
        json.dump(ingredient_dict, file, indent=4, ensure_ascii=False)

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
    
recipe_by_ingredient("Cacao")
#main()