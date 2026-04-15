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

## Supported File Types

- `.pdf`
- `.txt`

---

## Author

Built by Charles Lima 