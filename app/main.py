from fastapi import FastAPI
from rag.pipeline import run_pipeline

app = FastAPI()

# Dummy placeholders (initialize properly)
vector_store = None
bm25 = None

@app.get("/")
def home():
    return {"message": "RAG system running"}

@app.post("/query")
def query_api(query: str):
    result = run_pipeline(query, vector_store, bm25)
    return {"response": result}