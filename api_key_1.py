import time
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def timer(function):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()

        time_passed = f"{end - start:.6f} sec"

        return {
            "data": result,
            "time": time_passed
        }
    return wrap

@timer
def detect_language(text: str) -> str:
    """
    This function sends the given text to Gemini and
    Gemini returns the language of the text.
    The function should only return the language name (e.g. "English").
    """
    
    api_key_env = os.getenv("api_key")
    
    client = genai.Client(api_key = api_key_env)

    prompt = f"Analyze the following text and return only the language name:\n\n{text}"

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text.strip()

text = detect_language("This is a test sentence.")
print(text)