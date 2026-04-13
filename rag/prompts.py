def get_prompt(context, query):
    return f"""
You are an AI assistant. Answer the question based only on the context.

Context:
{context}

Question:
{query}

Answer:
"""