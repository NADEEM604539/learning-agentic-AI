from langchain_community.document_loaders import PyPDFLoader , WebBaseLoader

loader = PyPDFLoader("Nadeem-Mushtaq_Resume.pdf")

# docs = loader.load()
# web_url = WebBaseLoader('https://reference.langchain.com/python/langchain-community/document_loaders')

# data = web_url.load()
# print(docs[1].page_content)
# print(data)