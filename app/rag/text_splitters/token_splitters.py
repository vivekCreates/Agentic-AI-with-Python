from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text_splitter = TokenTextSplitter(
    chunk_size=100,
    chunk_overlap=1
)


data = PyPDFLoader("app/rag/sample.pdf")
docs = data.load()

chunks = text_splitter.split_documents(docs)
print(chunks[0])