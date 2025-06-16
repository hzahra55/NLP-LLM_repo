from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv


import os
load_dotenv()
# load documents
# loader = TextLoader('use_cases.txt')
# documents= loader.load()
# # text splitting 
# splitter=CharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=10
# )
# docs= splitter.split_documents(documents)

# # generate mebedings and store in DB
embeddings= OpenAIEmbeddings()
index_name= "data-store"
# vectorstore=PineconeVectorStore.from_documents(
#     docs,
#     index_name= index_name ,
#     embedding=embeddings
# )

# add more records
# url= "https://jobseeker.asendia.ai/practice-interview"
# loader2= WebBaseLoader(url)

# documents2= loader2.load()
# docs2=splitter.split_documents(documents2)

# vectorstore=PineconeVectorStore(
#     index_name=index_name,
#     embedding=embeddings
# )
# vectorstore.add_documents(docs2)

query="what product are they promoting?"
# response=vectorstore.similarity_search(query)
# print(response[0].page_content)
# response=vectorstore.similarity_search(query, filter={'source':"use_cases.txt"})
# print(response[0].page_content)
texts=["Here is some text about a product we are promoting."]



vectorstore=PineconeVectorStore.from_texts(
    texts,
    index_name=index_name,
    embedding=embeddings,
    namespace='sample_text'
)
# vectorstore.add_texts(['this is newly added text'],namespace='sample_text')
response=vectorstore.similarity_search(query, namespace='sample_text')
print(response)