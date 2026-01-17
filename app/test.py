import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()

embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query("hello world")

print(len(vector))
