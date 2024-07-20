import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 0.1,        # Lower temperature reduces randomness
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
text = """
concatenated text
"""


number = 10
type = "short answer"
level="easy"
topic="Red Hat redboot"
question = f"""
Imagine you are a teacher who has explained the topic {topic} from the above text to a 20-year-old student. Now refer to the above text and frame {number} {level} level {type} questions in the below format. Please avoid any additional text, instructions, or characters like "*" or "#", etc. in your response. Provide the response in the format below.

**
1. Question1 ?
**
**
2. Question2 ?
**


"""
response = (chat_session.send_message(text + question)).text
# print(question)
print(f"{response}")