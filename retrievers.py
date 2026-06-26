import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_classic.retrievers.document_compressors import LLMChainFilter
from langchain_classic.retrievers import MultiQueryRetriever, ContextualCompressionRetriever

os.environ["HF_HOME"] = "E:\\huggingface_embedding_cache"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True},
)

llm = ChatOpenAI(
    model="gpt-4.1-mini",  # Your Azure deployment name
    base_url="https://openai-rg-nadeem.openai.azure.com/openai/v1",
    # api_key=
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

ret= vectorStore.as_retriever(search_type= "mmr",search_kwargs={"k": 4})
# multiquery_retriever = MultiQueryRetriever.from_llm(
#     retriever=ret,
#     llm=llm,
# )

compressor = LLMChainFilter.from_llm(llm)
retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever= ret
)
results = retriever.invoke('tell me about skills of person')

print(results[1])