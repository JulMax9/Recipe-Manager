# Recipe-Manager
recipe manager built with python

# Recipe Manager

A command-line recipe management application built with Python for organizing and analyzing cooking recipes.

## Features

- **Add Recipes**: Store recipe name, ingredients list, cooking time, and servings
- **View Recipes**: Display all saved recipes with details
- **Delete Recipes**: Remove recipes by selection
- **Recipe Count**: Show total number of stored recipes
- **Longest Cooking Time**: Find the recipe that takes longest to prepare
- **Cooking Time Breakdown**: Categorize recipes by preparation time (Quick/Medium/Long)
- **Data Persistence**: Automatically saves and loads recipes using JSON

## What I Learned

### Core Concepts
- Working with lists of dictionaries
- Dynamic list building (ingredients)
- Input validation with try/except blocks
- Multi-field data management
- Categorization and data aggregation

### Technical Skills
- JSON file handling (save/load)
- Error handling for user input
- Function organization and structure
- Data filtering and analysis
- Working with nested data structures

### Problem-Solving
- Implementing data categorization logic
- Managing complex user input flows
- Handling edge cases (empty lists, invalid selections)
- Building intuitive menu systems

## How to Run
```bash
python3 recipeManager.py
```

## Requirements

- Python 3.x
- No external libraries required (uses built-in `json` module)

## Usage

1. Run the program
2. Choose from the menu:
   - `1` - Add a new recipe
   - `2` - Delete a recipe
   - `3` - View all recipes
   - `4` - See total recipe count
   - `5` - Find longest cooking time
   - `6` - View recipes by cooking time category
   - `7` - Save and quit

3. Data automatically saves when you quit and loads on next run

## Recipe Categories

Recipes are automatically categorized by cooking time:
- **Quick**: ≤ 10 minutes
- **Medium**: 11-30 minutes
- **Long**: > 30 minutes

## Example
```
1. Add recipe:
2. Delete recipe:
3. View recipe:
...

Select from the menu: 1
Enter your recipe name: Pasta Carbonara
Enter ingredients: pasta
Add another ingredient?(yes/no): yes
Enter ingredients: eggs
Add another ingredient?(yes/no): yes
Enter ingredients: bacon
Add another ingredient?(yes/no): no
Enter the cooking time: 25
Enter the number of servings: 4
```

## Project Structure
```
recipe-manager/
├── recipeManager.py      # Main application
└── recipeManager.json    # Data storage (created automatically)
```

## Skills Demonstrated

- Python fundamentals
- Data structure manipulation
- File I/O with JSON
- Comprehensive error handling
- User input validation
- Data categorization and analysis
- Clean code organization

## Challenges Overcome

- Implementing dynamic ingredient list building
- Creating cooking time categorization logic
- Managing complex data structures
- Ensuring data persistence across sessions

---

**Part of my Python learning journey** 🚀

*This is my second data management project, building on concepts from my Expense Tracker.*
