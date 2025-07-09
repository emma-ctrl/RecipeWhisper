# test_pipeline.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.pipeline import RecipeWhisperPipeline

def test_pipeline_with_transcript():
    print("=== Testing Complete Pipeline (Transcript Only) ===")
    
    pipeline = RecipeWhisperPipeline()
    
    # Test with a more complex transcript
    complex_transcript = """
    Welcome back to my kitchen! Today I'm excited to show you how to make 
    the perfect banana bread. This recipe serves about 8 people and takes 
    about an hour total.
    
    For ingredients, you'll need 3 ripe bananas, 1 and a half cups of 
    all-purpose flour, 3/4 cup of sugar, 1/3 cup of melted butter, 
    1 egg, 1 teaspoon of baking soda, and a pinch of salt.
    
    Let's start by preheating the oven to 350 degrees Fahrenheit. 
    While that's heating up, mash those bananas in a large bowl. 
    Next, mix in the melted butter with the mashed bananas. 
    Add the sugar, egg, and vanilla - mix well. 
    In a separate bowl, whisk together the flour, baking soda, and salt. 
    Gradually add the dry ingredients to the wet ingredients, stirring until just combined. 
    Pour the batter into a greased 9x5 inch loaf pan. 
    Bake for 60 to 65 minutes, or until a toothpick inserted in the center comes out clean. 
    Let it cool in the pan for 10 minutes before removing.
    """
    
    try:
        recipe = pipeline.process_transcript_only(complex_transcript)
        
        print(f"Recipe Title: {recipe.title}")
        print(f"Ingredients Found: {len(recipe.ingredients)}")
        print(f"Instructions: {len(recipe.instructions)}")
        
        print("\n=== Ingredients ===")
        for ingredient in recipe.ingredients:
            amount_unit = f"{ingredient.amount} {ingredient.unit}" if ingredient.amount else ""
            print(f"• {amount_unit} {ingredient.name}")
        
        print("\n=== Instructions ===")
        for step in recipe.instructions:
            print(f"{step.step_number}. {step.instruction}")
            
    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    test_pipeline_with_transcript()