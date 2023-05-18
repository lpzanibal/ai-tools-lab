import os
import re
from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings

load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="indexes",
                     embedding_function=embeddings)

pdf_files = [file for file in os.listdir('documents/') if re.match(r"^[a-zA-Z0-9_.-]+\.pdf$", file)]

loader = PyPDFLoader("resources/document.pdf")
pages = [*loader.load_and_split()]

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


# import sqlite3

# with open('Chinook_Sqlite.sql', 'r', -1, 'utf-8') as chinook_sql_file:
#     chinook_sql = chinook_sql_file.read()

# db = sqlite3.connect('chinook.db')
# cursor = db.cursor()
# cursor.executescript(chinook_sql)
# db.commit()
# db.close()
