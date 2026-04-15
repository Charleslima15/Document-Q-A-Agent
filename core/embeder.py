import dotenv
from google import genai
import chromadb


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
    chroma_client = chromadb.PersistentClient(path="chroma_store/")
    
    chroma_client.delete_collection("documents")
    collection = chroma_client.get_or_create_collection(name="documents")
    for i, item in enumerate(embedded_chunks):
        
        collection.add(
            ids=[f"text_{i}"],
            embeddings=[item["embedding"]],
            documents=[item["text"]]
        )
    
    print(f"Stored {len(embedded_chunks)} chunks in ChromaDB")


def retrieve_relevant_chunks(question, n_results=3):
    
    # Step 1: embed the question (you've done this before)
    question_embedding = client.models.embed_content(
            model="gemini-embedding-001",
            contents=question
        ).embeddings[0].values
    # Step 2: open chromadb and get the collection (you've done this before)
    chroma_client = chromadb.PersistentClient(path="chroma_store/")
    collection = chroma_client.get_or_create_collection(name="documents")
    
    # Step 3: query the collection
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )   
    
    # Step 4: return the texts
    return results['documents'][0]
  



