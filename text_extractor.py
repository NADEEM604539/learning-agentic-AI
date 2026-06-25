from langchain_community.document_loaders import PyPDFLoader , WebBaseLoader, DirectoryLoader

# loader = PyPDFLoader("Nadeem-Mushtaq_Resume.pdf")

# docs = loader.load()
# web_url = WebBaseLoader('https://reference.langchain.com/python/langchain-community/document_loaders')

# data = web_url.load()
# print(docs[1].page_content)
# print(data)

# lazy_docs = loader.lazy_load()

# for docs in lazy_docs:
#     print(docs)


loader = DirectoryLoader(
    "",
    glob= "**/*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
    print(doc)
