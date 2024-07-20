import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)
generation_config = {
    "temperature": 0.1,
    "top_p": 1.0,
    "top_k": 0,
    "max_output_tokens": 10000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(history=[])

def get_explanation(text, concept):
    question = f"""
    Imagine you are a teacher explaining the topic {concept} from the below text to a 20-year-old student.

Refer to the below text completely and explain the concept in depth at an intermediate level (not too easy, not too complex), including a definition and explanation.
Explain each and every important point mentioned about the {concept} in the text.
Provide an example.
Offer an analogy to further clarify the concept.
The response should not contain any "*" or "#" or any highlighted headings like * **Definition:**
Please avoid overloading with extra information and do not include any additional introductory text or characters like "*" or "#", etc.
Please use simple terms for in-depth explanation.

Make sure to return the response in the below format.

"
--Pluripotent stem cells are like master cells that have the potential to develop into almost any type of cell in the body. Imagine them as blank slates that can be programmed to become specialized cells, like muscle cells, nerve cells, or blood cells. 

--Think of it like this:  Imagine a single piece of clay. You can mold that clay into any shape you want - a cup, a plate, a sculpture.  Pluripotent stem cells are like that clay. They can be guided to become different types of cells, depending on the signals they receive.

--Definition: Pluripotent stem cells are undifferentiated cells that have the ability to develop into any cell type in the body, except for cells that make up the placenta. 

--Self-renewal: Pluripotent stem cells can divide and create more copies of themselves, maintaining a pool of undifferentiated cells.

--Differentiation: They can be induced to differentiate into specialized cell types, like muscle cells, nerve cells, or blood cells.

--Potential for therapeutic applications: Pluripotent stem cells hold great promise for treating diseases and injuries by replacing damaged or diseased cells.

--Example: Embryonic stem cells are a type of pluripotent stem cell found in early embryos. These cells have the potential to develop into any cell type in the body.

--Analogy: Imagine a tree. The seed is like a pluripotent stem cell. It has the potential to grow into a whole tree with branches, leaves, and roots. The seed can be guided to develop into different parts of the tree depending on the environment and signals it receives. 

Text:
{text}
    """
    response = chat_session.send_message(question)
    return response.candidates[0].content.parts[0].text

if __name__ == "__main__":
    concept = sys.argv[1]
    file_path = sys.argv[2]

    # Read the concatenated text from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        concatenated_text = file.read().strip()

    explanation = get_explanation(concatenated_text, concept)
    
    # Ensure output is printed in utf-8 encoding
    sys.stdout.buffer.write(explanation.encode('utf-8'))
