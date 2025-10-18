# POC - Bridge of Knowledge 🤖  
**Proof of Concept (POC) Submission**

This POC is an interactive AI tutor that answers user questions using **Retrieval-Augmented Generation (RAG)**. It extracts relevant information from uploaded **PDF, Excel, and Text files** to provide **accurate, source-based answers**. The goal of this prototype is to demonstrate how conversational AI can support education and document intelligence.

---

## ✅ Objective

This POC demonstrates:

- AI-powered document question answering  
- Multi-format input support (**PDF, Excel, Text**)  
- Reliable responses using **RAG architecture**  
- Conversational memory for contextual dialogue  
- Local **FAISS vector database** for semantic search  
- Simple and expandable architecture  

---

## ✨ Key Features

| Feature | Description |
|----------|-------------|
| 📚 Multi-format Support | Upload and query **PDFs, Excel spreadsheets, and text files** |
| 🔁 Conversation Memory | Stores chat history to improve follow-up questions |
| 🔍 Document-Grounded Answers | Reduces hallucination with fact-based retrieval |
| ⚡ Fast Search | Semantic retrieval using FAISS |
| 🖥️ User-Friendly UI | Web app built with Streamlit |
| 🔧 Flexible Architecture | Add more docs anytime – automatically indexed |

---

## 📥 Supported File Types

| File Type | Extensions | Example Use Case |
|-----------|------------|------------------|
| PDF | `.pdf` | Books, reports, manuals |
| Excel | `.xlsx`, `.xls` | Data sheets, tabular reports |
| Text | `.txt` | Notes, summaries |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language Model | OpenAI GPT |
| Framework | LangChain |
| Vector Store | FAISS |
| File Processing | `unstructured`, `pandas` |
| Frontend | Streamlit |
| Language | Python |
| Environment | `uv` |

---
1. Clone the Repository

git clone https://github.com/YourUsername/YourRepositoryName.git
cd YourRepositoryName

2. Create and Activate Virtual Environment This project uses uv for environment management.

# Create the virtual environment
uv venv

# Activate the environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
3. Install Dependencies Install all the required Python packages from requirements.txt.

UV_TIMEOUT=120 uv pip install -r requirements.txt
4. Set Up Your API Key You need an OpenAI API key to run the tutor.

Create a file named .env in the root of the project directory.
Add your API key to this file:
OPENAI_API_KEY="sk-..."
5. Add Your Documents

Place the PDF files you want the tutor to learn from inside the THEMES IN WORLD HISTORY Textbook for Class XI directory.
The first time you run the application, it will automatically process these files and create a faiss_index_from_unstructured directory to store the knowledge base.
🚀 How to Run
You can run the application as a web app or directly in the command line.

Web App (Recommended) To launch the user-friendly Streamlit interface, run:

streamlit run app.py
Command-Line Interface To interact with the tutor directly in your terminal, run:

python VidyaSetu.py
☁️ Deployment
This application is ready for deployment on Streamlit Community Cloud. To deploy:

Push your entire project to a public GitHub repository (including the directory with your PDFs).
Make sure your .gitignore file includes .env to protect your API key.
Connect your GitHub repository to Streamlit Community Cloud and add your OPENAI_API_KEY in the advanced settings under "Secrets".
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
