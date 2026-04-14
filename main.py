import dotenv
import os
from google import genai
from core.loaderr import load_and_chunk
from core.embeder import embed_chunks


dotenv.load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello, are you working?"
)

print(response.text)

# chunks = load_and_chunk("docs/myFile.txt")
# print(chunks[0])
# print("---")

chunks = load_and_chunk("docs/myFile.txt")
embedded = embed_chunks(chunks)

print(f"Number of embedded chunks: {len(embedded)}")
print(f"First chunk text: {embedded[0]['text'][:100]}")
print(f"Embedding length: {len(embedded[0]['embedding'])}")
print(type(embedded[0]['embedding']))
print(embedded[0]['embedding'])




