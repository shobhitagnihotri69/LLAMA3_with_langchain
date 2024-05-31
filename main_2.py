import os 
from dotenv import load_dotenv, find_dotenv
load_dotenv()
print(f"Current working directory: {os.getcwd()}")
dotenv_path = find_dotenv()
print(f"Dotenv path: {dotenv_path}")
from langchain.llms import ollama
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'