
from pathlib import Path




def load_and_chunk(filepath, chunk_size=500):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) <= chunk_size:
            current_chunk += " " + word
        else:
            chunks.append(current_chunk)
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk)

    print(f"Total chunks created: {len(chunks)}")
    return chunks