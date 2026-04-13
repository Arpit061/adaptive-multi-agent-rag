import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)

    def add(self, vectors):
        self.index.add(np.array(vectors).astype("float32"))

    def search(self, query_vector, k=5):
        return self.index.search(np.array(query_vector).astype("float32"), k)