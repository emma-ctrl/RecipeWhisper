# this is where the Pydnatic models (which defines the LLMs structured output) live

from pydantic import BaseModel
from typing import List, Optional

# represents a single recipe ingredient
class Ingredient(BaseModel):
    name: str
    amount: Optional[str] = None
    unit: Optional[str] = None

# represents a single cooking instruction
class Step(BaseModel):
    step_number: int
    instruction: str

# ties the whole recipe together 
class Recipe(BaseModel):
    title: str
    ingredients: List[Ingredient]
    instructions: List[Step]