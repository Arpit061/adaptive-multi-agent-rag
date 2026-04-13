#print("retriever file loaded")


def retrieve(query, vectorstore, embed_fn, chunks, k=5):
    q_vec = embed_fn([query])
    scores, indices = vectorstore.search(q_vec, k)
    return [chunks[i] for i in indices[0]]