# this is the main file that users can run

import sys
from src.pipeline import RecipeWhisperPipeline

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <youtube_url>")
        print("Example: python main.py https://www.youtube.com/watch?v=abc123")
        return
    
    youtube_url = sys.argv[1]
    
    print("RecipeWhisper - Converting YouTube cooking videos to structured recipes")
    print(f"Processing: {youtube_url}")
    print("-" * 60)
    
    pipeline = RecipeWhisperPipeline()
    
    try:
        recipe = pipeline.process_youtube_video(youtube_url)
        
        print("\n" + "="*60)
        print("RECIPE EXTRACTED SUCCESSFULLY!")
        print("="*60)
        
        print(f"\n**{recipe.title}**")
        
        print(f"\n**Ingredients ({len(recipe.ingredients)}):**")
        for ingredient in recipe.ingredients:
            amount_unit = f"{ingredient.amount} {ingredient.unit}" if ingredient.amount else ""
            print(f"• {amount_unit} {ingredient.name}")
        
        print(f"\n **Instructions ({len(recipe.instructions)}):**")
        for step in recipe.instructions:
            print(f"{step.step_number}. {step.instruction}")
        
        print("\n" + "="*60)
        print("Recipe saved! You can now cook this dish!")
        
    except Exception as e:
        print(f"\n Error: {e}")
        print("Please check the YouTube URL and try again.")

if __name__ == "__main__":
    main()