from langchain_chroma import Chroma
import os 
os.environ["HF_HOME"] = "E:\\huggingface_embedding_cache"
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language 
from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_experimental.text_splitter import SemanticChunker

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True},
)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
pdf_load = PyPDFLoader('Nadeem-Mushtaq_Resume.pdf')
# pdfs = DirectoryLoader(
#     "",
#     glob="**/*.pdf",
#     loader_cls=PyPDFLoader
# )

docs = pdf_load.load()

text = text_splitter.split_documents(docs)


# vectorStore= Chroma.from_documents(
#     documents=text,
#     embedding=embeddings,
#     collection_name="my_docs",
#     persist_directory='./verctor_store'
# )


vectorStore = Chroma(
    collection_name="my_docs",
    embedding_function=embeddings,
    persist_directory="./verctor_store",
)

results= vectorStore.similarity_search('list out skills of that person and what is his name and details', k=2)
print(results)