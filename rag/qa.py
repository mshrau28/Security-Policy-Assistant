from rag.retriever import retrieve_query
from rag.confidence import confidence_score
from rag.llm_chain import chain

def answer_question(question):
    results = retrieve_query(question)

    confidence, score = confidence_score(results)

    if confidence == "Low":
         return {
             "answer": "Insufficient evidence",
             "confidence": confidence
         }

    context = "\n\n".join(
        doc.page_content for doc, _ in results
    )

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    return {
        "answer": answer,
        "confidence": confidence
    }
