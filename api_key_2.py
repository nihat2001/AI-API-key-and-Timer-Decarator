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
def change_tone(text: str, tone: str = "formal") -> str:
    """
    This function rewrites the given text in the specified tone.
    The tone parameter can be "formal", "casual", or "technical".
    """
    
    api_key_env = os.getenv("api_key")
    
    client = genai.Client(api_key = api_key_env)

    prompt = f"You are a professional editor. Without any introductory or explanatory sentences, rewrite the following text in {tone} tone: {text}"

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text.strip()

text = change_tone("This is a test sentence.", "formal")
print(text)