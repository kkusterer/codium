import random
import os

restaurants = [
    "Harves", "Leos", "Pierce road", "Bob evens", "Nories", "Gs pizza",
    "Fire house", "Sombreos", "Famous daves", "Blossoms", "Sushi n",
    "Red lobster", "Texas roadhouse", "Logans", "2nd street", "Rio lunas",
    "Chen's buffet", "Outback", "Bevers", "H20", "Os", "Luckies",
    "Qudoba", "Chilies", "Codeys landings", "Noodles and company",
    "Huannas", "Buffalo wild wings",
]

while True:
    try:
        os.system("cls" if os.name == "nt" else "clear")
        number = int(input("how many places: "))
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(number):
            pick = random.choice(restaurants)
            print(f"Random pick {i + 1}: {pick}")
        print()
        
        input("press enter to continue")

    except ValueError:
        print("enter a number")
