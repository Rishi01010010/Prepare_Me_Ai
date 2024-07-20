import os
from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 0.1,        # Lower temperature reduces randomness
    "top_p": 1.0,              # Setting top_p to 1 disables nucleus sampling
    "top_k": 0,                # Setting top_k to 0 disables top-k sampling
    "max_output_tokens": 20000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# File path
file_path = "D:\\Module-4 Notes (1).pdf"

# Question prompt
question = """list down the important concepts mentioned in this text in the below format.
Make sure that you don't repeat the topics/concepts twice or more.
1. Tom
2. Jerry
3. Bob
without any additional text"""

def get_pdf_page_count(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            return len(pdf.pages)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def extract_pdf_text_and_store(file_path):
    page_count = get_pdf_page_count(file_path)
    if page_count is None:
        return page_count
    
    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            for i in range(page_count):
                page_text = pdf.pages[i].extract_text()
                globals()[f'a{i + 1}'] = page_text  # Dynamically create and assign variables
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
    return page_count

def concatenate_page_texts(page_count):
    concatenated_text = ""
    for i in range(1, page_count + 1):
        variable_name = f'a{i}'
        if variable_name in globals():
            concatenated_text += globals()[variable_name] + " "
    return concatenated_text.strip()

def get_important_concepts(file_path, question):
    page_count = extract_pdf_text_and_store(file_path)
    if page_count:
        concatenated_text = concatenate_page_texts(page_count)
        response = chat_session.send_message(concatenated_text + " " + question)
        return response.candidates[0].content
    else:
        return "Failed to extract text from PDF."

# Example usage
important_concepts = get_important_concepts(file_path, question)
print(important_concepts)
