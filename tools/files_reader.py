#External files reader tool

#With   Pypdf
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
from langchain_core.tools import tool


load_dotenv()

@tool
def read_pdf(file_path: str) -> str:
    """
    Read the content of a PDF file and return it as a string.

    Use this tool when:
    - you need to extract text from a PDF document
    - the user provides a PDF file and asks for its content or specific information from it

    Input:
        file_path: the path to the PDF file

    Output:
        The extracted text content of the PDF file as a string.
    """
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"An error occurred while reading the PDF: {e}"
    
#
# print(read_pdf.invoke("rag_db/Barrière linguistique aux événements internationaux _ enjeu économique.pdf"))