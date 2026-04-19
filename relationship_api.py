from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)


def get_advice(name: str, age: int, gender: str, duration: str, problem: str, topic: str) -> dict:
    """
    Returns a dict with:
      - advice: professional therapist-style advice (max 100 words)
      - activities: 3 suggested bonding activities
    """

    advice_prompt = f"""
You are a warm, professional couples therapist. 
The person seeking help is: {name}, {age} years old, {gender}, in a relationship for {duration}.
Their main concern area: {topic}
Their situation: {problem}

Give empathetic, practical advice in under 100 words.
Write in second person (you/your). Be warm but professional.
Do NOT use markdown headers — just flowing paragraphs.
Respond only in English.
"""

    activities_prompt = f"""
You are a couples therapist. Based on this couple's situation:
- Duration together: {duration}
- Problem area: {topic}
- Situation: {problem}

Suggest exactly 3 specific bonding activities they can do together to strengthen their relationship.
Format as a simple numbered list: 1. ... 2. ... 3. ...
Keep each activity under 30 words. Be creative and specific.
Respond only in English.
"""

    advice_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[advice_prompt]
    )

    activities_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[activities_prompt]
    )

    return {
        "advice": advice_response.text.strip(),
        "activities": activities_response.text.strip()
    }
