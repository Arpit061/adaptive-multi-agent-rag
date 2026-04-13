from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self, documents):
        self.texts = [doc.page_content for doc in documents]
        self.tokenized = [text.split() for text in self.texts]
        self.bm25 = BM25Okapi(self.tokenized)

    def retrieve(self, query, top_k=3):
        scores = self.bm25.get_scores(query.split())
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return [self.texts[i] for i in ranked[:top_k]]