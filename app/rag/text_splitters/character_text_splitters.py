from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

text_splitter = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=1
)


data = TextLoader("app/rag/text_splitters/notes.txt")
docs = data.load()

chunks = text_splitter.split_documents(docs)

for chunk in chunks:
    print(chunk.page_content)
    print()