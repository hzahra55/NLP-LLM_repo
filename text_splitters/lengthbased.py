from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

splitter= CharacterTextSplitter(
    chunk_size= 100,
    chunk_overlap=1,
    separator ="."
)

loader= PyPDFLoader("usecase.pdf")
docs= loader.load()
result= splitter.split_documents(docs)
print(result[1])