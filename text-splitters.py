from langchain_text_splitters import RecursiveCharacterTextSplitter, Language 
from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader
from langchain_experimental.text_splitter import SemanticChunker

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
pdf_load = PyPDFLoader('Nadeem-Mushtaq_Resume.pdf')
# pdfs = DirectoryLoader(
#     "",
#     glob="**/*.pdf",
#     loader_cls=PyPDFLoader
# )

# docs = pdfs.lazy_load()

text = text_splitter.split_documents(pdf_load)

# print(text)



