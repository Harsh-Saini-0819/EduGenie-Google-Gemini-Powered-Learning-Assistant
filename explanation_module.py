import os
from google import genai

def explain_concept(concept: str, depth: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Configuration Fault: GEMINI_API_KEY token is missing."
        
    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
        Explain the concept of '{concept}' tailored exactly to a target depth of: '{depth}'.
        Break down complex terminology into highly intuitive terms or practical real-world analogies.
        Use clear structural breakdown headers.
        """
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text if response.text else "Failed to produce text."
    except Exception as error:
        return f"Error executing Explanation Module: {str(error)}"
