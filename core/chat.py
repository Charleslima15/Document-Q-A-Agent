from google import genai

from core.embeder import retrieve_relevant_chunks


from google import genai

def ask(question):
    retrieved_chunks = retrieve_relevant_chunks(question)
    
    prompt = f"""Use the following context to answer the question.

Context:
{retrieved_chunks}

Question: {question}
Answer:"""

    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
