from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .tools import DocumentQATool
from pydantic import BaseModel

load_dotenv(find_dotenv())

class UserQuery(BaseModel):
    query: str

app = FastAPI()

@app.post("/tools/qa")
def document_qa(user_query: UserQuery):
    document_qa_tool = DocumentQATool()
    response = document_qa_tool.query(user_query.query)
    return {"response": response}

app.mount('/qa', StaticFiles(directory='./static', html=True), name='static')