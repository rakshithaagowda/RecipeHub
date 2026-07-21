import os

from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_recipe(ingredients):
    prompt = f"""
You are an expert chef and nutritionist.

The user has the following ingredients:

{ingredients}

Your task:
- Generate the best possible recipe using the given ingredients.
- You may use common kitchen essentials such as:
  - Salt
  - Pepper
  - Cooking oil
  - Butter
  - Water
  - Basic spices
- Do NOT add expensive or unrelated ingredients.
- Prefer popular recipes that people actually cook.
- Keep the recipe simple, practical, and easy for beginners.
- Prefer recipes that take less than 30 minutes whenever possible.
- If the ingredients are not enough for a complete recipe, politely mention what one or two additional ingredients would improve it.

Return ONLY in the following format:

Recipe Name:
<Recipe Name>

Ingredients:
- Ingredient 1
- Ingredient 2
- Ingredient 3

Steps:
1. Step one
2. Step two
3. Step three

Cooking Time:
<Time>

Calories (Approx):
<Calories>

Tips:
<One useful cooking tip>

Do NOT include:
- Chef notes
- Introductions
- Explanations
- Markdown formatting
- Bold text
- Bullet decorations other than "-"
- Any text outside the requested format
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text