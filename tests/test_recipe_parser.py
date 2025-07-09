# test_recipe_parser.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.recipe_parser import RecipeParser

def test_recipe_parser():
    print("=== Testing Recipe Parser ===")
    
    parser = RecipeParser()
    print("Recipe parser initialized")
    
    # Mock transcript - like what we'd get from a cooking video
    mock_transcript = """
    Hi everyone! Today we're making chocolate chip cookies. 
    You'll need 2 cups of flour, 1 cup of butter, half a cup of sugar,
    and 1 cup of chocolate chips. 
    
    First, preheat your oven to 350 degrees. 
    Then mix the flour and sugar in a bowl. 
    Add the butter and mix until combined.
    Fold in the chocolate chips.
    Bake for 12 minutes until golden brown.
    """
    
    try:
        recipe = parser.parse_transcript(mock_transcript)
        print("Recipe parsed successfully!")
        print(f"Title: {recipe.title}")
        print(f"Ingredients: {len(recipe.ingredients)}")
        print(f"Instructions: {len(recipe.instructions)}")
        
        # Show the structured output
        print("\n=== Structured Recipe ===")
        print(recipe.model_dump_json(indent=2))
        
    except Exception as e:
        print(f"Recipe parsing failed: {e}")

if __name__ == "__main__":
    test_recipe_parser()