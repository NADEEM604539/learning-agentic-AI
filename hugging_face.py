import os 
os.environ["HF_HOME"] = "E:\\huggingface_cache"
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-1.5B-Instruct",
    task= "text-generation",
    pipeline_kwargs = dict(
        max_new_tokens= 512,
        do_sample= False,
        temperature= 1.3
    ),
)

chat_model = ChatHuggingFace(llm = llm)
