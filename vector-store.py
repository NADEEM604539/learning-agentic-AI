from langchain_chroma import Chroma
import os 
os.environ["HF_HOME"] = "E:\\huggingface_embedding_cache"
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True},
)

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
# pdf_load = PyPDFLoader('Nadeem-Mushtaq_Resume.pdf')

# docs = pdf_load.load()

# text = text_splitter.split_documents(docs)

persist_directory = './vector_store'

# vectorStore = Chroma.from_documents(
#     documents=text,
#     embedding=embeddings,
#     collection_name="my_docs",
#     persist_directory=persist_directory,
# )

vectorStore = Chroma(
    collection_name="my_docs",
    embedding_function=embeddings,
    persist_directory=persist_directory,
)

results= vectorStore.similarity_search('tell me tools and platforms', k=1)
print(results)