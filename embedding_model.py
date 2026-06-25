import os 
import numpy as np
os.environ["HF_HOME"] = "E:\\huggingface_embedding_cache"
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    encode_kwargs={"normalize_embeddings": True},
)

doc = [
    "hello how are you",
    "i am finee",
    "i am nadeem"
]

# Query to find the best match
query = "how are you"
query_result = embeddings.embed_query(query)
doc_embed = embeddings.embed_documents(doc)

# Calculate cosine similarity between query and each document
similarities = [np.dot(query_result, doc_vec) for doc_vec in doc_embed]

# Find the document with the highest similarity
best_match_idx = np.argmax(similarities)
matching_doc = doc[best_match_idx]
matching_similarity = similarities[best_match_idx]

# Print results
print(f"Query: '{query}'")
print(f"Best matching string: '{matching_doc}'")
print(f"Similarity score: {matching_similarity:.4f}")

