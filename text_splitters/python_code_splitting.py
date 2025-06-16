from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Load the Markdown file
loader = TextLoader("use_case.md", encoding="utf-8")
docs = loader.load()

# Create the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,        # you can adjust this
    chunk_overlap=50,      # this ensures smoother context transitions
    separators=["\n\n", "\n", " ", ""]
)

# Split the documents into chunks
chunks = splitter.split_documents(docs)

# Display chunk info
print(f"Total Chunks: {len(chunks)}\n")

# Print the chunks
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.page_content)
    print()


"""
splitter= RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size=100,
    chunk_overlap=2
)

chunks= splitter.split_text(text)

print(chunks[0])