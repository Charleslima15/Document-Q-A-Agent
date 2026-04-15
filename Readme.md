# Doc Agent — Chat With Any Document Using AI

A command-line RAG (Retrieval Augmented Generation) system built in Python that lets you upload any PDF or text file and ask it questions in plain English.

---

## What It Does

You point it at a document. It reads it, understands it, and lets you have a conversation with it. Ask it anything about the content and it will find the relevant parts and answer you.

---

## Tech Stack

- **Python 3.10+**
- **Google Gemini API** — for embeddings and text generation
- **ChromaDB** — local vector database
- **PyMuPDF** — PDF text extraction
- **python-dotenv** — environment variable management

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/doc_agent.git
cd doc_agent
```

**2. Install dependencies**
```bash
pip install google-generativeai chromadb pymupdf python-dotenv
```

**3. Add your Gemini API key**

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_key_here
```

Get a free API key at [aistudio.google.com](https://aistudio.google.com)

---

## Usage

```bash
python main.py
```

You will be prompted to enter the path to your document:
```
Enter the path to your document: docs/yourfile.pdf
```

Then start asking questions:
```
You: What is the main argument of this document?
Agent: ...

You: Summarize the second section
Agent: ...

You: quit
```

Type `quit` to exit.

---

## Supported File Types

- `.pdf`
- `.txt`

---

## Important Notes

- Each time you load a new document, the previous document's data is cleared from ChromaDB automatically
- Your API key is never hardcoded — it lives only in your `.env` file
- The `chroma_store/` folder is created automatically on first run

---

## What I Learned Building This

This was my first real Python project. I learned how embeddings work, how vector databases store and retrieve meaning, and how RAG systems are structured. Every bug — especially the ChromaDB data pollution issue — taught me something a tutorial never could.

---

## Author

Built by Charles Lima 