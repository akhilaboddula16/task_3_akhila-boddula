from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from backend.config import GROQ_API_KEY, GROQ_MODEL


def generate_summary_dashboard(documents):
    text = ""

    for doc in documents[:20]:
        page = doc.metadata.get("page_number", "Unknown")
        text += f"\n[Page {page}]\n{doc.page_content}\n"

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0.1
    )

    prompt = ChatPromptTemplate.from_template("""
You are a legal document analyst.

Create a Summary Dashboard using ONLY the document text.
Do not make up facts.
Every point must mention page number.

Document Text:
{text}

Return exactly in this format:

## Document Summary
- ...

## Risks
- Risk:
  Evidence:
  Page:

## Important Dates
- Date:
  Meaning:
  Page:

## Stakeholders
- Name/Party:
  Role:
  Page:

## Key Clauses
- Clause:
  Explanation:
  Page:

## Missing or Unclear Information
- ...
""")

    response = llm.invoke(
        prompt.format_messages(text=text)
    )

    return response.content