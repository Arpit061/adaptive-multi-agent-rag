def simple_rerank(docs, query):
    # Simple heuristic (can replace with cross-encoder later)
    return docs[:3]