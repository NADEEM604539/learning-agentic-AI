# Learning AI Project

## Overview

This repository is a record of my learning journey with **LangChain**, **RAG**, **advanced RAG**, and **LangGraph**.

The project is not just a code dump. It shows how I moved from simple LLM calls to embeddings, vector search, retrieval pipelines, tool usage, structured outputs, and graph-based orchestration.

The repo is split into three main parts:

- **Root files**: LangChain experiments, RAG pipelines, embeddings, prompt templates, tools, models, and vector store work
- **`langgraph/`**: graph workflows, persistence, time travel, subgraphs, memory, and advanced RAG notebooks
- **assets/data**: PDFs, text files, screenshots, and vector store folders used during experiments

---

## What this project covers

This project includes work on:

- LLM model setup with **OpenAI Azure** and **Hugging Face**
- Prompt templates and message handling
- Embeddings and similarity search
- PDF loading and document extraction
- Text splitting and chunking
- Vector stores with **Chroma**
- Retriever strategies
- Contextual compression and multi-query retrieval
- Tool creation and tool calling
- Basic LangGraph workflows
- Conditional routing and branching
- Parallel execution
- Persistence and memory
- Time travel / state inspection
- Subgraphs
- Basic RAG and advanced RAG techniques like **CRAG** and **Self-RAG**

---

## Root directory overview

### `Readme.md`
Current project documentation and learning overview.

### `requirements.txt`
Lists the main packages used in the project, including:
- `langchain-core`
- `langchain-community`
- `langchain-huggingface`
- `langgraph`
- `chromadb`
- `pypdf`
- `bs4`
- `transformers`
- `torch`

### `model.py`
Runs a **Hugging Face chat model** using `Qwen/Qwen2.5-1.5B-Instruct` through `ChatHuggingFace` and `HuggingFacePipeline`.

### `hugging_face.py`
Creates the Hugging Face pipeline-backed chat model used by other scripts.

### `azure_chat.py`
Uses **Azure OpenAI** with `ChatOpenAI` and a prompt template to test Azure-hosted chat completion.

### `prompt_template.py`
Shows basic prompt template usage and message setup.

### `embedding_model.py`
Demonstrates embeddings and similarity scoring with `HuggingFaceEmbeddings` and NumPy dot-product matching.

### `text_extractor.py`
Loads PDF documents using `PyPDFLoader` and `DirectoryLoader` for document ingestion experiments.

### `text-splitters.py`
Experiments with `RecursiveCharacterTextSplitter` on the resume PDF for chunking text into smaller pieces.

### `vector-store.py`
Creates and queries a **Chroma vector store** from embedded PDF chunks.

### `retrievers.py`
Uses retriever strategies such as:
- `as_retriever()`
- **MMR** search
- **MultiQueryRetriever**
- **ContextualCompressionRetriever**
- `LLMChainFilter`

This is one of the main files for the RAG and advanced retrieval work.

### `tools.py`
Defines custom tools using `@tool` and `StructuredTool` for arithmetic operations.

### `tools_calling.py`
Demonstrates **tool calling** with an LLM, including binding tools, invoking them, reading tool calls, and combining tool outputs with the model response.

### `text.txt`
Plain text data used in experimentation.

### `Nadeem-Mushtaq_Resume.pdf` / `Nadeem-Mushtaq_Resume copy.pdf`
Resume PDFs used as the source document for PDF loading, splitting, embeddings, retrieval, and RAG testing.

### `Screenshot 2026-06-20 172647.png`
Reference screenshot saved in the project.

### `vector_store/` and `verctor_store/`
Persisted Chroma vector store folders used during retrieval experiments.

### `.env`
Environment file for keys and local configuration.

### `.git/`, `.gitignore`, `.vscode/`, `venv/`, `__pycache__/`
Project and environment support folders.

---

## LangChain and RAG learning path

### 1. Model setup
I started by connecting to different model backends:
- Azure OpenAI chat models
- Hugging Face pipelines

This helped me understand how to switch between providers and how model configuration works.

### 2. Prompting and structured interaction
I learned how to:
- Build prompt templates
- Pass variables into prompts
- Use messages for chat-style workflows
- Think about outputs in a structured way

### 3. Embeddings
I explored embeddings using `HuggingFaceEmbeddings` to understand how text is converted into vectors and how semantic similarity works.

### 4. Document ingestion
I loaded PDFs and experimented with extracting content from documents so that unstructured files could become searchable knowledge sources.

### 5. Chunking and splitting
I used text splitters to break large documents into smaller chunks for retrieval and vector indexing.

### 6. Vector stores
I stored embedded chunks in **Chroma** so the project could perform semantic search over document content.

### 7. Retrieval
I tested retrievers and learned how retrieval improves LLM answers by fetching relevant context before generation.

### 8. Advanced retrieval
I expanded retrieval with:
- **MMR** to improve diversity
- **MultiQueryRetriever** to generate multiple search angles
- **ContextualCompressionRetriever** to reduce noise
- **LLMChainFilter** to keep only the most relevant results

This is where the project moves beyond basic RAG into **advanced RAG**.

### 9. Tools and tool calling
I learned how to define tools, bind them to an LLM, inspect tool calls, and execute them.

---

## LangGraph folder overview

The `langgraph/` folder contains the workflow and memory side of the project.

### Python workflow files

- `sequentical_workflow.py` — basic step-by-step graph execution
- `parallel_workflow.py` — branching into multiple nodes in parallel
- `condition_workflow.py` — conditional routing based on state values
- `persistance.py` — graph persistence and checkpointing with memory
- `time_travelling.py` — inspecting and resuming prior graph states
- `fault_tolerance.py` — recovery and safer workflow behavior

### Notebook workflows

- `notebook.ipynb` — general LangGraph experimentation
- `tools.ipynb` — tool usage inside LangGraph
- `RAG.ipynb` — basic LangGraph + retrieval/RAG flow
- `iterative_workflow.ipynb` — repeated/looping graph execution
- `subgraph.ipynb` — subgraph-based design
- `subgraph_type2.ipynb` — alternate subgraph implementation
- `condition_jupiter.ipynb` — conditional graph notebook
- `persistance.ipynb` — persistence notebook version
- `time_travelling.ipynb` — time-travel and checkpoint exploration
- `fault_tolerance.ipynb` — fault-tolerance experiments

### Memory folder

- `memory/short_term.ipynb` — short-term memory handling
- `memory/long_term.ipynb` — long-term memory concepts
- `memory/longterm_example.ipynb` — long-term memory example workflow

### Advanced RAG folder

- `advance_rag/CRAG.ipynb` — **Corrective RAG (CRAG)**
- `advance_rag/SelfRAG.ipynb` — **Self-RAG**
- `advance_rag/correctiveRAG.png` — visual reference for CRAG
- `advance_rag/SELF-RAG.png` — Self-RAG reference image
- `advance_rag/SELF-RAG-GRAPH.png` — graph diagram for Self-RAG
- `advance_rag/data.txt` — supporting data for the advanced RAG notebooks
- `advance_rag/vectorStore/` — vector store used in advanced RAG work

---

## LangGraph concepts learned

From the LangGraph part of the project, I learned:

- How to define graph state with `TypedDict`
- How nodes pass and update state
- How `START` and `END` control execution
- How conditional edges work
- How to build parallel execution paths
- How to checkpoint and resume workflows
- How to inspect state history
- How to handle time-travel style debugging
- How subgraphs help structure larger systems
- How memory changes graph behavior over multiple turns

---

## Advanced RAG concepts covered

The project includes more than basic retrieval. It also touches advanced retrieval design such as:

- **CRAG**: correcting or refining retrieval before generation
- **Self-RAG**: the model evaluates or improves its own retrieval behavior
- Retriever compression
- Query expansion
- Relevance filtering
- Better context selection
- Vector-store backed search over document collections

These files show that the project is not only about loading documents, but about improving retrieval quality and answer quality.

---

## Full learning outcome

By building this project, I learned:

- How LLM apps are assembled from smaller pieces
- How embeddings and vector databases support semantic search
- How RAG pipelines are built and improved
- How advanced retrieval techniques make answers more reliable
- How tools extend model capabilities
- How LangGraph adds workflow control, memory, and branching
- How to think in terms of systems instead of single prompts

---

## Why this project matters

This project reflects my progress from:

1. Basic model testing
2. Prompt engineering
3. Embeddings and retrieval
4. Basic RAG
5. Advanced RAG
6. Tools and function calling
7. LangGraph orchestration
8. Persistence, memory, and time travel

It shows practical experimentation and a real understanding of how modern LLM applications are built.

---

## Future improvements

Possible next steps:

- Add a diagram for each LangGraph workflow
- Turn the scripts into cleaner modules
- Add README notes for each notebook
- Add tests for retriever and tool logic
- Create one end-to-end assistant that combines RAG, tools, and LangGraph
- Clean up duplicate or temporary vector store folders

---

## Summary

This repository is my personal AI learning lab.

It contains:
- LangChain experiments
- RAG and advanced RAG implementations
- Tool calling examples
- Hugging Face and Azure model setup
- LangGraph workflows
- Memory, persistence, and branching examples

The project shows the full journey from simple prompts to advanced retrieval and graph-based AI systems.