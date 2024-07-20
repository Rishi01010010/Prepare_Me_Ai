import sys
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 0.0,        # Lower temperature reduces randomness
    "top_p": 1.0,              # Setting top_p to 1 disables nucleus sampling
    "top_k": 0,                # Setting top_k to 0 disables top-k sampling
    "max_output_tokens": 10000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(history=[])

def answer_question(text, question):
    response = chat_session.send_message(text + " " + question)
    return response.candidates[0].content.parts[0].text

if __name__ == "__main__":
    text = sys.argv[1]
    concept = sys.argv[2]
    explanation = sys.argv[3]
    question = sys.argv[4]

    complete_text = f"Please keep your responses concise, ideally no longer than two lines unless necessary. Here was your explanation on the topic {concept}:\n{explanation}\n\nI'll be asking some questions regarding this concept. Please answer the following question about '{concept}':\n"
    answer = answer_question(complete_text, question)
    print(answer)
