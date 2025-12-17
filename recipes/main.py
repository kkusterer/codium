import recipes
import os
import recipe_list
import random_recipe

recipes_list = {
    "grilled cheese sandwich": recipes.recipe_1,
    "scrambled eggs": recipes.recipe_2,
    "peanut butter and jelly sandwich": recipes.recipe_3,
    "pancakes": recipes.recipe_4,
    "spaghetti with marinara sauce": recipes.recipe_5,
    "chicken quesadilla": recipes.recipe_6,
    "garden salad": recipes.recipe_7,
    "baked chicken breast": recipes.recipe_8,
    "oatmeal": recipes.recipe_9,
    "chocolate chip cookies": recipes.recipe_10,
}

while True:
    os.system("cls" if os.name == "nt" else "clear")

    choice = input( 
        "Enter recipe name or get list of recipes(l) or random recipe generator(r) or type 'exit': " 
        ).lower().strip()

    os.system("cls" if os.name == "nt" else "clear")

    if choice in recipes_list:
        recipes_list[choice]()

    elif choice == "l":
        recipe_list.recipe_list()

    elif choice == "r":
        random_recipe.random_recipe()

    elif choice == "exit":
        os.system("cls" if os.name == "nt" else "clear")
        break
    

    else: 
        print("Not a recipe")
        input("Press Enter to continue...")
