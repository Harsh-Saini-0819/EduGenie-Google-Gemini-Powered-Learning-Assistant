import os
from transformers import pipeline

# Fallback pipeline using a local CPU-friendly text generator model
try:
    local_generator = pipeline("text2text-generation", model="MBZUAI/LaMini-Flan-T5-248M")
except Exception:
    local_generator = None

def generate_quiz(context: str, num_questions: int) -> str:
    # If API key is available, use Gemini for high-fidelity formatting; otherwise fall back cleanly to local model
    api_key = os.getenv("GEMINI_API_KEY")
    
    if api_key:
        from google import genai
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"""
            Based on the context provided below, generate exactly {num_questions} multiple-choice questions.
            Do NOT show the correct answer immediately after the question. 
            
            Instead, output the quiz in TWO distinct sections separated EXACTLY by the text '|||ANSWERKEY|||'.
            
            Section 1: The questions and options only. Format:
            Q1: [Question text]
            A) [Option 1]
            B) [Option 2]
            C) [Option 3]
            D) [Option 4]
            
            Section 2: The correct answer letters only. Format:
            1: A
            2: C
            3: B
            
            CONTEXT:
            {context}
            """

            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            return response.text if response.text else "Empty response payload."
        except Exception as err:
            return f"Gemini Engine Error: {str(err)}"
            
    # Local model execution fallback strategy
    if local_generator:
        try:
            input_text = f"Generate {num_questions} quiz questions about: {context[:500]}"
            res = local_generator(input_text, max_length=512)
            return res[0]['generated_text']
        except Exception as local_err:
            return f"Local Inference Failure: {str(local_err)}"
            
    return "Error: No Gemini API Key configured and local HuggingFace weights could not be loaded."
