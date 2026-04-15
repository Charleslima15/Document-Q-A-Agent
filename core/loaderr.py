from pathlib import Path
import pymupdf

def load_and_chunk(filepath, chunk_size=500):
    filepath = Path(filepath)
    
    if filepath.suffix == ".txt":
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
    elif filepath.suffix == ".pdf":
        text = ""
        doc = pymupdf.open(filepath)
        for page in doc:
            text += page.get_text()
        doc.close()
    else:
        raise ValueError(f"Unsupported file type: {filepath.suffix}")
    
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