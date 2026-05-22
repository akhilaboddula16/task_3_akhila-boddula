from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from backend.config import GROQ_API_KEY, GROQ_MODEL


def build_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0.1
    )

    prompt = ChatPromptTemplate.from_template("""
You are a professional legal document analyst.

Your task is to answer questions using ONLY the provided context.

Rules:
1. Do not use outside knowledge.
2. Do not hallucinate or make up facts.
3. If the answer is not found in the context, say:
   "I could not find this information in the uploaded document."
4. Every answer must include page number citations.
5. Keep the answer clear and professional.

Context:
{context}

Question:
{question}

Answer format:

Answer:
<your answer>

Citations:
- Page <page_number>: <short supporting evidence>
""")

    def answer_question(question: str):
        docs = retriever.invoke(question)

        context = ""

        for doc in docs:
            page = doc.metadata.get("page_number", "Unknown")
            context += f"\n[Page {page}]\n{doc.page_content}\n"

        response = llm.invoke(
            prompt.format_messages(
                context=context,
                question=question
            )
        )

        return response.content, docs

    return answer_question