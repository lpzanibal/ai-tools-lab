from dotenv import load_dotenv, find_dotenv
from langchain import HuggingFacePipeline, PromptTemplate, LLMChain, HuggingFaceHub
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.vectorstores import Chroma

load_dotenv(find_dotenv())

# INSTRUCT EMBEDDINGS PRUEBA
# embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")
# query_result = embeddings.embed_query("This is a test document.")
# print(query_result)
# vectorstore = Chroma(
#     embedding_function=OpenAIEmbeddings(),
#     persist_directory="indexes/openai")
# collection = vectorstore.get()
# print(
#         f"Ahora hay {len(collection['ids'])} elementos en la VectorDB")
# retriever = vectorstore.as_retriever()
# docs = retriever.get_relevant_documents("cual es el articulo 8?")
# print(len(docs))

# CORRER HF LOCAL
# model = "bigscience/bloom-560m"
# temperature = 0.8

# llm = HuggingFacePipeline.from_model_id(model_id=model, task="text-generation", model_kwargs={
#     "temperature": temperature, "max_length": 100})

# print(llm("The BLOOM large language model is a"))


# template = """Question: {question}

# Answer: Let's think step by step."""
# prompt = PromptTemplate(template=template, input_variables=["question"])

# model_id = 'gpt2-medium'

# ###Simple
# llm = HuggingFacePipeline.from_model_id(model_id=model_id, task="text-generation", model_kwargs={
#                                         "temperature": 1e-6, "max_length": 100})

# #Avanzado
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)

# pipe = pipeline(
#     "text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     max_length=100
# )

# llm = HuggingFacePipeline(pipeline=pipe)


# ###LLM CHAIN
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "What is the capital of England?"

# print(llm_chain.run(question))


# para usar embeddings locales https://colab.research.google.com/drive/1h2505J5H4Y9vngzPD08ppf1ga8sWxLvZ?usp=sharing


# from langchain.llms import HuggingFacePipeline
# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM

# model_id = 'google/flan-t5-large'# go for a smaller model if you dont have the VRAM
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# pipe = pipeline(
#     "text2text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     max_length=100
# )

# local_llm = HuggingFacePipeline(pipeline=pipe)
