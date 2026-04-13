

def generate_answer(query, context):
    return f"""
    Answer:
    {context}

    (Generated based on retrieved context)

    Question: {query}
    """