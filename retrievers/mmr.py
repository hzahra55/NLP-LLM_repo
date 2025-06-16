from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

docs=[
  Document(page_content="OpenAI provides a powerful API for language generation, called GPT-4. "),
  Document(page_content="LangChain is a framework that simplifies working with LLMs in production. "),
  Document(page_content="MMR stands for Maximal Marginal Relevance, a ranking method that balances relevance and diversity. "),
  Document(page_content=" Pinecone is a vector database optimized for similarity search at scale."),
  Document(page_content="OpenAI also offers embeddings through models like text-embedding-ada-002 "),
  Document(page_content="MMR helps avoid redundancy in results by penalizing similar content when ranking chunks. "),
  Document(page_content=" You can use LangChain with Pinecone and OpenAI to build intelligent RAG systems."),
  
 ]

embedding= OpenAIEmbeddings()

vectorstore= FAISS.from_documents(
    documents=docs,
    embedding=embedding

)

retriever = vectorstore.as_retriever(
                        search_type="mmr",
                        search_kwargs={'k':3, "lambda_mult":0}


)

query= "what is langchain?"
results= retriever.invoke(query)

for i, doc in enumerate (results):
    print(f"--- {i+1} ---")
    print(doc.page_content)