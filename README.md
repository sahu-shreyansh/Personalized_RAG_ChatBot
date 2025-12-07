
# 🧠 Personalized – AI Tutor (RAG Powered)
An interactive personalized assistance system designed to answer your queries by extracting information from uploaded learning materials. Using **Retrieval-Augmented Generation (RAG)**, the system ensures that answers are **fact-grounded, contextual, and traceable** to source files.

## 🎯 Objective
This Project demonstrates how AI can support educational content delivery by:
- Understanding student questions and referencing book content directly
- Reducing hallucinations with retrieval-based answers
- Maintaining conversation context
- Accepting multiple document formats
- Offering a scalable and modular architecture

## ✨ Key Features
| Feature | Description |
|--------|-------------|
| 📚 Multi-Source Document Support | Accepts PDFs, Excel sheets, and text notes |
| 🔍 RAG-based AI Retrieval | Accurate answers based on document embeddings |
| 🧠 Conversational Memory | Sustains follow-up context without re-asking |
| ⚡ FAISS Vector Store | Fast semantic search for large documents |
| 🖥️ Streamlit Interface | Clean and intuitive student-friendly UI |
| 🔄 Auto Document Indexing | New files are processed and embedded automatically |

## 📥 Supported File Formats
| Format | Extensions | Use Case |
|--------|------------|----------|
| PDF | `.pdf` | NCERT books, manuals, guides |
| Excel | `.xlsx`, `.xls` | Tabular historical timelines, datasets |
| Text | `.txt` | Notes, summaries, extracted content |

## 🛠️ Tech Stack
| Component | Technology |
|-----------|------------|
| LLM | OpenAI GPT |
| Retrieval | FAISS (local) |
| Framework | LangChain |
| Document Parsing | `unstructured`, `pandas` |
| Frontend | Streamlit |
| Environment | `uv` |
| Language | Python |

## 📦 Setup & Installation
### 1. Clone Repository
```bash
git clone https://github.com/YourUsername/YourRepositoryName.git
cd YourRepositoryName
```

### 2. Create Virtual Environment
```bash
uv venv
```

### 3. Activate Environment
```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
UV_TIMEOUT=120 uv pip install -r requirements.txt
```

### 5. Configure API Key
Create `.env` in project root:
```env
OPENAI_API_KEY="sk-..."
```

## 📚 Add Documents
Place textbooks and other learning files here:
```
THEMES IN WORLD HISTORY Textbook for Class XI/
```
The system will automatically create:
```
faiss_index_from_unstructured/
```
on first run to store embeddings and metadata.

## 🚀 Run the Application
### Web Interface (recommended)
```bash
streamlit run app.py
```

### Command Line Mode
```bash
python VidyaSetu.py
```

## ☁️ Deployment (Streamlit Cloud)
1. Push repository to GitHub  
2. **Do not include `.env`**
3. Add ***OPENAI_API_KEY*** under **Secrets → Advanced Settings**
4. Deploy directly from GitHub

## 📄 License
This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

## 🧩 Future Enhancements
- Dashboard with learning analytics
- Support for image-based textbooks using OCR
- Multiple-chapter and multi-subject expansion
- Voice-enabled Q&A system
- Adaptive learning progress tracking

## 🙌 Contribution
Contributions are welcome!  
Feel free to open an issue, fork the repository, or submit a PR.
