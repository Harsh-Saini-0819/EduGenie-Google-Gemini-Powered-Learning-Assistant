import os
from google import genai

def generate_summary(text: str, format_style: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Runtime Error: Missing operational GEMINI_API_KEY environment variable."
        
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
        Summarize the following source text. The output style must strictly align with: '{format_style}'.
        Ensure no vital structural arguments or formulas are omitted.
        
        TEXT:
        {text}
        """
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text if response.text else "Summary generation could not return valid tokens."
    except Exception as e:
        return f"Summary Engine Exception: {str(e)}"
