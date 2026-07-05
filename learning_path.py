import os
from google import genai

def design_path(goal: str, timeframe: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Authorization Fault: API Key missing from execution parameters."
        
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
        Act as an elite educational planner. Design a highly structural, personalized learning pathway to master: '{goal}'.
        The complete milestone progression blueprint must fit entirely within a timeline restriction of: '{timeframe}'.
        Break down instructions by phase/week with strict, measurable objectives.
        """
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text if response.text else "Could not generate milestones."
    except Exception as err:
        return f"Learning Path Architecture Exception: {str(err)}"
