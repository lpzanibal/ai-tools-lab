from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings

load_dotenv(find_dotenv())

def store_embeddings(texts, embedding_function, path):
    vectorstore = Chroma.from_documents(
        texts, embedding_function, persist_directory=path)
    collection = vectorstore.get()
    print(
        f"Ahora hay {len(collection['ids'])} elementos en la VectorDB ({path})")

# Preparar datos

loader = DirectoryLoader('documents/', glob="./*.pdf", loader_cls=PyPDFLoader)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200)
texts = text_splitter.split_documents(documents)
print(f"Cargando {len(texts)} textos...")

# Crear y almacenar embeddings (HuggingFace, Instruct-base y OpenAI)

# store_embeddings(texts, HuggingFaceEmbeddings(), "indexes/huggingface")
store_embeddings(texts, HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base"), "indexes/instruct-base")
# store_embeddings(texts, OpenAIEmbeddings(), "indexes/openai")


# import sqlite3

# with open('Chinook_Sqlite.sql', 'r', -1, 'utf-8') as chinook_sql_file:
#     chinook_sql = chinook_sql_file.read()

# db = sqlite3.connect('chinook.db')
# cursor = db.cursor()
# cursor.executescript(chinook_sql)
# db.commit()
# db.close()
