# this is where the text transcript is converted into structured output (following the pydantic sturcture from models.py) using the the LLM

# src/recipe_parser.py
import openai
import json
import os
from dotenv import load_dotenv
from src.models import Recipe
from pydantic import ValidationError

load_dotenv()

class RecipeParser:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def parse_transcript(self, transcript: str) -> Recipe:
        """Convert a transcript into a structured Recipe object"""
        
        # This is the prompt that tells the LLM how to structure the output
        prompt = f"""
        Extract a structured recipe from this cooking video transcript. 
        Pay close attention to:
        - Ingredient names, amounts, and units
        - Step-by-step instructions in the correct order
        - Any cooking times or temperatures mentioned
        
        Transcript:
        {transcript}
        
        Format your response as a JSON object with this exact structure:
        {{
            "title": "Recipe Name Here",
            "ingredients": [
                {{"name": "ingredient name", "amount": "quantity", "unit": "measurement"}},
                {{"name": "ingredient name", "amount": "quantity", "unit": "measurement"}}
            ],
            "instructions": [
                {{"step_number": 1, "instruction": "detailed instruction here"}},
                {{"step_number": 2, "instruction": "detailed instruction here"}}
            ]
        }}
        
        Make sure step numbers are sequential starting from 1.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3  # Low temperature for consistent output
            )
            
            # Parse the JSON response
            recipe_json = response.choices[0].message.content
            recipe_data = json.loads(recipe_json)
            
            # Use Pydantic to validate and create Recipe object
            recipe = Recipe(**recipe_data)
            return recipe
            
        except json.JSONDecodeError as e:
            raise Exception(f"LLM returned invalid JSON: {e}")
        except ValidationError as e:
            raise Exception(f"Recipe validation failed: {e}")
        except Exception as e:
            raise Exception(f"Recipe parsing failed: {e}")