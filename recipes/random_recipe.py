import recipes
import random
import os

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


def random_recipe():
    name, func = random.choice(list(recipes_list.items()))
    print(f"Random pick: {name.title()}\n")
    func()

