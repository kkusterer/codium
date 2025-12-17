import os

def done():
    while True:
        end = input("are you finished (y/n)")
        if end.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            break
        if end.lower() == "n":
            ...
        else:
            print("pick n or y")

 
def recipe_1():
    print("Title: Grilled Cheese Sandwich")
    print("Total Time: 10 min , Cook Time: 5 min, Prep Time: 5 min")
    print("Ingreadents: Bread, Butter, Cheddar Cheese")
    print("Step 1: Butter one side of each slice of bread.")
    print("Step 2: Place cheese between unbuttered sides.")
    print("Step 3: Heat pan over medium heat.")
    print("Step 4: Cook until golden brown on both sides.")
    print("Step 5: Remove, slice, and serve.")
    done()


def recipe_2():
    print("Title: Scrambled Eggs")
    print("Total Time: 7 min , Cook Time: 5 min, Prep Time: 2 min")
    print("Ingreadents: Eggs, Butter, Salt, Pepper")
    print("Step 1: Crack eggs into a bowl.")
    print("Step 2: Whisk with salt and pepper.")
    print("Step 3: Melt butter in a pan.")
    print("Step 4: Cook eggs on low heat, stirring.")
    print("Step 5: Remove when soft and fluffy.")
    done()


def recipe_3():
    print("Title: Peanut Butter & Jelly Sandwich")
    print("Total Time: 5 min , Cook Time: 0 min, Prep Time: 5 min")
    print("Ingreadents: Bread, Peanut Butter, Jelly")
    print("Step 1: Place bread slices on a plate.")
    print("Step 2: Spread peanut butter on one slice.")
    print("Step 3: Spread jelly on the other slice.")
    print("Step 4: Press slices together.")
    print("Step 5: Cut and serve.")
    done()


def recipe_4():
    print("Title: Pancakes")
    print("Total Time: 20 min , Cook Time: 15 min, Prep Time: 5 min")
    print("Ingreadents: Pancake Mix, Milk, Egg, Butter")
    print("Step 1: Mix pancake mix, milk, and egg.")
    print("Step 2: Heat buttered pan on medium heat.")
    print("Step 3: Pour batter into pan.")
    print("Step 4: Flip when bubbles form.")
    print("Step 5: Cook until golden and serve.")
    done()


def recipe_5():
    print("Title: Spaghetti with Marinara Sauce")
    print("Total Time: 25 min , Cook Time: 20 min, Prep Time: 5 min")
    print("Ingreadents: Spaghetti, Marinara Sauce, Salt")
    print("Step 1: Boil water with salt.")
    print("Step 2: Cook spaghetti until al dente.")
    print("Step 3: Heat marinara sauce.")
    print("Step 4: Drain spaghetti.")
    print("Step 5: Combine pasta with sauce and serve.")
    done()


def recipe_6():
    print("Title: Chicken Quesadilla")
    print("Total Time: 15 min , Cook Time: 10 min, Prep Time: 5 min")
    print("Ingreadents: Tortilla, Cooked Chicken, Cheese")
    print("Step 1: Heat pan over medium heat.")
    print("Step 2: Place tortilla in pan.")
    print("Step 3: Add cheese and chicken.")
    print("Step 4: Fold tortilla in half.")
    print("Step 5: Cook until crispy and serve.")
    done()


def recipe_7():
    print("Title: Garden Salad")
    print("Total Time: 10 min , Cook Time: 0 min, Prep Time: 10 min")
    print("Ingreadents: Lettuce, Tomato, Cucumber, Dressing")
    print("Step 1: Wash all vegetables.")
    print("Step 2: Chop lettuce, tomato, and cucumber.")
    print("Step 3: Add vegetables to a bowl.")
    print("Step 4: Add dressing.")
    print("Step 5: Toss and serve.")
    done()


def recipe_8():
    print("Title: Baked Chicken Breast")
    print("Total Time: 30 min , Cook Time: 25 min, Prep Time: 5 min")
    print("Ingreadents: Chicken Breast, Olive Oil, Salt, Pepper")
    print("Step 1: Preheat oven to 375°F.")
    print("Step 2: Coat chicken with oil and seasoning.")
    print("Step 3: Place chicken in baking dish.")
    print("Step 4: Bake until fully cooked.")
    print("Step 5: Rest for 5 minutes and serve.")
    done()


def recipe_9():
    print("Title: Oatmeal")
    print("Total Time: 8 min , Cook Time: 5 min, Prep Time: 3 min")
    print("Ingreadents: Oats, Water or Milk, Salt")
    print("Step 1: Bring water or milk to a boil.")
    print("Step 2: Add oats and salt.")
    print("Step 3: Reduce heat and simmer.")
    print("Step 4: Stir occasionally.")
    print("Step 5: Serve warm.")
    done()


def recipe_10():
    print("Title: Chocolate Chip Cookies")
    print("Total Time: 25 min , Cook Time: 12 min, Prep Time: 13 min")
    print("Ingreadents: Flour, Sugar, Butter, Eggs, Chocolate Chips")
    print("Step 1: Preheat oven to 350°F.")
    print("Step 2: Mix butter and sugar.")
    print("Step 3: Add eggs and dry ingredients.")
    print("Step 4: Stir in chocolate chips.")
    print("Step 5: Bake until golden brown.")
    done()

