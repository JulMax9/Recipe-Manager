import json

recipes = []

def add_recipe():
    name = input("Enter your recipe name: ")
    
    ingredients = []
    while True:
        new_ingredient = input("Enter ingredients: ")
        ingredients.append(new_ingredient)
        
        again = input("Add another ingredient?(yes/no): ")
        if again.lower() != "yes":
            break 
    
    while True:
        try:
           cooking_time = int(input("Enter the cooking time: "))
           if cooking_time > 0:
               break
           else:
                print("Enter an actual cooking time")
        except ValueError:
            print("Oops, enter a integer")
    while True:
        try:
            servings = int(input("Enter the number of servings: "))
            if servings > 0:
                break
            else:
                print("Enter an actual number of servings")
        except ValueError:
            print("Oops, enter an integer")

    recipes.append({

        "name": name,
        "ingredients": ingredients,
        "cooking_time": cooking_time,
        "servings": servings

        })
def delete_recipe():
    if len(recipes) == 0:
        print("Recipe is still null")
        return

    print("\nAvailable Recipes: ")
    for index, rec in enumerate(recipes, start=1):
        print(f"{index}. {rec['name']} ({rec['cooking_time']} min)")

    try:
        select = int(input("Enter the recipe number you want to delet: "))

        if select < 1 or select > len(recipes):
            print("Enter a Valid number")
            return
        
        deleted_recipe = recipes.pop(select - 1)
        print(f"\nRecipe '{deleted_recipe['name']}' Successfully Deleted!")
           
    except ValueError:
        print("Oops, supposed to enter an actual number")
    
def view_recipe():
    if len(recipes) == 0:
        print("Recipe is still null")
        return
    else:
        for index, rec in enumerate(recipes, start=1):
            print(f"{index}. {rec['name']}: {rec['ingredients']}, {rec['cooking_time']}, {rec['servings']}")

def total_recipe():
    if len(recipes) == 0:
        print("Recipe is still null")
        return
    print(f"You have {len(recipes)} recipes available")

def longest_cooking_time():
    if len(recipes) == 0:
        print("Recipe still null")
        return
    else:
        high_cook_time = recipes[0]
        for rec in recipes:
            if rec["cooking_time"] > high_cook_time["cooking_time"]:
                high_cook_time = rec
    return high_cook_time
    
def cooking_time_breakdown():
    if len(recipes) == 0:
        print("Recipe still null")
        return {"Quick": [], "Medium": [], "Long": []} # return empty disc
    time_breakdown = {
        "Quick": [],
        "Medium": [],
        "Long": []

        }
    for rec in recipes:
        if rec["cooking_time"] <= 10:
            time_breakdown["Quick"].append(rec)
        elif rec["cooking_time"] <= 30:
            time_breakdown["Medium"].append(rec)
        else:
            time_breakdown["Long"].append(rec)
            
    return time_breakdown

breakdown = cooking_time_breakdown()

for category, rec in breakdown.items():
    print(f"\n{category} recipes:")
    for r in rec:
        print(f"-{r['name']} ({r['cooking_time']} mins)")
            
def save_to_file():
    if len(recipes) == 0:
        print("No recipes to save")
        return
    
    with open("recipeManager.json", "w") as f:
        json.dump(recipes, f, indent=4)
        print("Recipes Saved")

def load_from_file():
    try:
        with open("recipeManager.json", "r") as f:
            global recipes
            recipes = json.load(f)
            print(f"loaded {len(recipes)} recipes")
    except FileNotFoundError:
        print("No saved file found, strarting fresh.")
        

load_from_file()

while True:
    options = ["Add recipe:",
               "Delete recipe:",
               "View recipe:",
               "Total recipe:",
               "Longest Cooking Time:",
               "Cooking Time breakdown",
               "Save & Quit: "
               ]

    for index, opts in enumerate(options, start=1):
        print(f"{index}. {opts}")

    try:
        choice = int(input("Select from the menu: "))
        if choice == 1:
            add_recipe()
        elif choice == 2:
            delete_recipe()
        elif choice == 3:
            view_recipe()
        elif choice == 4:
            total_recipe()
        elif choice == 5:
            result = longest_cooking_time()
            if result:
               print(f"Longest cooking time: {result['name']} - {result['cooking_time']} mins")
        elif choice == 6:
            breakdown = cooking_time_breakdown()
            for category, rec in breakdown.items():
                print(f"\n{category} recipes:")
                for r in rec:
                   print(f"-{r['name']} ({r['cooking_time']} mins)")
                  
        elif choice == 7:
            save_to_file()
            print("Done already, Bye!")
            break
        else:
            print("Wrong Input Entered.")
    except ValueError:
        print("Failure to input an actual Value")

    
    


            
            
    
    

        
