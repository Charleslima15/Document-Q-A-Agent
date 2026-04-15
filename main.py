import dotenv
from core.loaderr import load_and_chunk
from core.embeder import embed_chunks, store_embeddings
from core.chat import ask

dotenv.load_dotenv()

# Run these two lines only once to load your document
filepath = input("Enter the path to your document: ")
chunks = load_and_chunk(filepath)
embedded = embed_chunks(chunks)
store_embeddings(embedded)

# Chat loop
while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
    answer = ask(question)
    print(f"Agent: {answer}\n")