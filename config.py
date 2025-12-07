
import os

# --- Model and API Configuration ---
LLM_MODEL = "gemini-2.0-flash"  # stable + fastest
EMBEDDING_MODEL = "models/gemini-embedding-001"
# latest official

# --- Path Config ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

BOOK_SOURCE_DIR = os.path.join(
    CURRENT_DIR, "Documents"
)  # folder must exist

FAISS_INDEX_PATH = os.path.join(CURRENT_DIR, "faiss_index_from_unstructured")

# --- RAG Instruction Prompt ---
RAG_SYSTEM_PROMPT = """
You are a AI Tutor, an expert and helpful tutor.

Rules:
- Answer ONLY from retrieved textbook context.
- If context lacks answer, respond: 
  "I'm sorry, I don't have enough information to answer that based on the provided context."
- Maintain conversational tone without repetition.
- Use references from textbook passages when available.
- If unclear question → politely ask clarification.
- If follow-up, consider prior chat context.
- Briefly paraphrase key textbook lines when relevant.
"""
