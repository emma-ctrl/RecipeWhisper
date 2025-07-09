# test_step_by_step.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.models import Recipe, Ingredient, Step
from src.audio_extractor import AudioExtractor

def test_models():
    print("=== Testing Pydantic Models ===")
    
    # Create a simple recipe manually
    recipe = Recipe(
        title="Test Recipe",
        ingredients=[
            Ingredient(name="flour", amount="2", unit="cups"),
            Ingredient(name="sugar", amount="1", unit="cup")
        ],
        instructions=[
            Step(step_number=1, instruction="Mix ingredients"),
            Step(step_number=2, instruction="Bake for 30 minutes")
        ]
    )
    
    print(f"Recipe created: {recipe.title}")
    print(f"Ingredients: {len(recipe.ingredients)}")
    print(f"Steps: {len(recipe.instructions)}")
    
    # Test JSON serialization
    json_output = recipe.model_dump_json(indent=2)
    print("JSON output:")
    print(json_output)

def test_audio_extractor():
    print("\n=== Testing Audio Extractor ===")
    
    extractor = AudioExtractor()
    print("Audio extractor initialized")
    print(f"Download path: {extractor.download_path}")
    
    # We'll test with a real URL later
    print("Ready to extract audio from YouTube")

if __name__ == "__main__":
    test_models()
    test_audio_extractor()