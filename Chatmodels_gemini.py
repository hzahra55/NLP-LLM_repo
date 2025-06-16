from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result= model.invoke("when is the best time to drink water in day?")

print(result.content)