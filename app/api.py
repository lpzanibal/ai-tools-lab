from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .tools import DocumentQATool, QueryDBTool

load_dotenv(find_dotenv())

class UserQuery(BaseModel):
    query: str

app = FastAPI()

@app.post("/tools/document-qa")
def document_qa(user_query: UserQuery):
    document_qa_tool = DocumentQATool()
    response = document_qa_tool.query(user_query.query)
    return {"response": response.strip()}

@app.post("/tools/query-db")
def query_db(user_query: UserQuery):
    query_db_tool = QueryDBTool()
    response = query_db_tool.query(user_query.query)
    return {"response": response.strip()}

app.mount('/document-qa', StaticFiles(directory='./static/document-qa', html=True), name='document-qa')
app.mount('/query-db', StaticFiles(directory='./static/query-db', html=True), name='query-db')