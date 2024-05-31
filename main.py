from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title= "Langchain -server",
    version= "1.0",
    description= 'A simple AI sever '
)
from fastapi import APIRouter
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['Langchain_api_key'] = os.getenv('Langchain_api_key')
llm = 'llama3' 
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
model = ChatOllama(model = llm, temperature= 0)
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")
from langserve import add_routes
add_routes(app ,
            model|prompt,
              path = '/joke' )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)

