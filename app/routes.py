from fastapi import APIRouter
from rag.pipeline import run_pipeline

from ingestion.loader import load_documents
from ingestion.chunking import chunk_documents
from ingestion.embedding import get_embeddings
from vectorstore.faiss_store import create_vector_store
from vectorstore.bm25 import BM25Retriever

router = APIRouter()

# --- Initialize once ---
docs = load_documents("data/raw/sample.pdf")
chunks = chunk_documents(docs)

embeddings = get_embeddings()
vector_store = create_vector_store(chunks, embeddings)

bm25 = BM25Retriever(chunks)


@router.get("/")
def home():
    return {"message": "RAG system running"}


@router.post("/query")
def query_api(query: str):
    response = run_pipeline(query, vector_store, bm25)
    return {"response": response}