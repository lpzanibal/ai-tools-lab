import os
import re
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA, SQLDatabaseChain
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase

class DocumentQATool:

    def __init__(self):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma(
            persist_directory="indexes", embedding_function=embeddings)

        if len(vectorstore.get()["ids"]) == 0:
            pdf_files = [file for file in os.listdir('documents/') if re.match(r"^[a-zA-Z0-9_.-]+\.pdf$", file)]
            pages = []

            for file in pdf_files:
                loader = PyPDFLoader("documents/" + file)
                pages = [*pages, *loader.load_and_split()]

            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
            )
            docs = text_splitter.split_documents(pages)
            vectorstore.add_documents(
                documents=docs, embedding=embeddings, persist_directory="indexes"
            )

        self.qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=vectorstore.as_retriever())

    def query(self, query):
        return self.qa_chain.run(query)

class QueryDBTool:

    def __init__(self):
        db = SQLDatabase.from_uri(os.environ["DB_URI"])
        self.db_chain = SQLDatabaseChain.from_llm(llm=OpenAI(temperature=0), db=db, verbose=True)

    def query(self, query):
        return self.db_chain.run(query)