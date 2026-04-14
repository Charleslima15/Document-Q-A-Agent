import dotenv
from google import genai

dotenv.load_dotenv()
client = genai.Client()
def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunk
        )
        
        embedding_dict = {"text": chunk, "embedding": result.embeddings[0].values}
        embeddings.append(embedding_dict)
    return embeddings

def store_embeddings(embedded_chunks):
    






