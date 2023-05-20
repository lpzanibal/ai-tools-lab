import os
from langchain.llms import OpenAI
from langchain import HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.sql_database import SQLDatabase
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import LLMChain, RetrievalQA, SQLDatabaseChain
from langchain.prompts import PromptTemplate


class DocumentQATool:

    def __init__(self):
        vectorstore = Chroma(
            persist_directory="indexes/openai", embedding_function=OpenAIEmbeddings())
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(), chain_type="stuff", retriever=vectorstore.as_retriever())

    def query(self, query):
        return self.qa_chain.run(query)


class QueryDBTool:

    def __init__(self):
        db = SQLDatabase.from_uri(os.environ["DB_URI"])
        self.db_chain = SQLDatabaseChain.from_llm(
            llm=OpenAI(temperature=0), db=db, use_query_checker=True)

    def query(self, query):
        return self.db_chain.run(query)


class HFPromptTool:

    def __init__(self, model, temperature=1e-6):
        self.llm = HuggingFaceHub(repo_id=model, model_kwargs={
            "temperature": temperature, "max_length": 100})

    def prompt(self, prompt):
        return self.llm(prompt)
