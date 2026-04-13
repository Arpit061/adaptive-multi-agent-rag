from ingestion.loader import load_documents
from ingestion.chunking import chunk_text
from ingestion.embedding import embed_chunks
from vectorstore.faiss_store import VectorStore
from rag.retriever import retrieve
from rag.generator import generate_answer

# Load
text = load_documents("data/raw/sample.txt")

# Chunk
chunks = chunk_text(text)

# Embed
embeddings = embed_chunks(chunks)

# Store
vs = VectorStore(len(embeddings[0]))
vs.add(embeddings)

# Query
query = "What is Artificial Intelligence?"

retrieved = retrieve(query, vs, embed_chunks, chunks)
unique_chunks = list(dict.fromkeys(retrieved))
unique_chunks = list(dict.fromkeys(retrieved))
context = "\n".join(unique_chunks[:2])  # take top 2 only

answer = generate_answer(query, context)

print("\nANSWER:\n", answer)