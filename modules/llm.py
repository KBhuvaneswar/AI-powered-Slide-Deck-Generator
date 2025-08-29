import os
import google.generativeai as genai
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# GEMINI_MODEL_NAME = "gemini-1.5-flash"

# def generate_text(prompt: str, temperature: float = 0.4) -> str:
#     """
#     Call Gemini API with a given prompt and return text response.
#     """
#     try:
#         model = genai.GenerativeModel(GEMINI_MODEL_NAME)
#         response = model.generate_content(prompt)
#         return response.text.strip()

#     except Exception as e:
#         print(f"[LLM Error] {e}")
#         return ""

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

GROQ_MODEL_NAME = "llama-3.1-8b-instant"   #llama3-8b-8192

def generate_text(prompt: str, temperature: float = 0.4) -> str:
    """
    Call Groq API with a given prompt and return text response.
    """
    try:
        response = client.chat.completions.create(
            model=GROQ_MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"[LLM Error] {e}")
        return ""

def summarize_article(article_text: str, source_title: str, topic: str) -> str:
    prompt = f"""
    You are an AI assitant, helping create a slide deck on '{topic}'.
    Summarize the following article in a clear and concise way.
    Highlight the main arguments, key insights, and conclusions. 
    Keep the summary under 250 words and write it in simple, easy-to-understand language. 
    Avoid unnecessary details but retain all essential points.
    Source title: {source_title}

    Text:
    {article_text[:6000]}  
    """                             # Limiting to first 6000 characters to avoid token limits
    return generate_text(prompt)

