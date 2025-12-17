import os
def recipe_list():
    print("grilled cheese sandwich")
    print("scrambled eggs")
    print("peanut butter and jelly sandwich")
    print("pancakes")
    print("spaghetti with marinara sauce")
    print("chicken quesadilla")
    print("garden salad")
    print("baked chicken breast")
    print("oatmeal")
    print("chocolate chip cookies")

    while True:
        end = input("are you finished (y/n)")
        if end.lower() == "y":
            os.system("cls" if os.name == "nt" else "clear")
            break
        if end.lower() == "n":
            ...
        else:
            print("pick n or y")
