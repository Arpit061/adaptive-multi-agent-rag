from rag.retriever import hybrid_retrieval
from rag.generator import generate_answer
from rag.prompts import get_prompt
from rag.reranker import simple_rerank
from agents.query_agent import rewrite_query
from agents.evaluation_agent import evaluate_response

def run_pipeline(query, vector_store, bm25):
    query = rewrite_query(query)

    docs = hybrid_retrieval(query, vector_store, bm25)
    docs = simple_rerank(docs, query)

    context = "\n".join(docs)
    prompt = get_prompt(context, query)

    response = generate_answer(prompt)

    if not evaluate_response(response, context):
        return "Low confidence response"

    return response