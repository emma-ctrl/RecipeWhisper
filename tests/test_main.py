# tests/test_main.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Mock the pipeline for testing
class MockPipeline:
    def process_youtube_video(self, url):
        from src.models import Recipe, Ingredient, Step
        return Recipe(
            title="Mock Recipe",
            ingredients=[
                Ingredient(name="flour", amount="2", unit="cups"),
                Ingredient(name="eggs", amount="2", unit="")
            ],
            instructions=[
                Step(step_number=1, instruction="Mix ingredients"),
                Step(step_number=2, instruction="Cook until done")
            ]
        )

# Test the main logic
def test_main_logic():
    pipeline = MockPipeline()
    recipe = pipeline.process_youtube_video("fake_url")
    
    print(f"Recipe: {recipe.title}")
    print(f"Ingredients: {len(recipe.ingredients)}")
    print(f"Instructions: {len(recipe.instructions)}")

if __name__ == "__main__":
    test_main_logic()