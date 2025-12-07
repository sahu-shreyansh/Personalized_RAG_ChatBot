import os
from typing import List

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai
from unstructured.partition.pdf import partition_pdf
import pandas as pd
import config


class RagSystem:
    """
    Clean & stable RAG system supporting PDF, TXT, XLSX.
    """

    def __init__(self):
        print("🚀 Initializing RAG System...")
        load_dotenv()
        self._validate_api_key()

        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=api_key)

        self.embedding_model = GoogleGenerativeAIEmbeddings(
            model=config.EMBEDDING_MODEL,
            google_api_key=os.getenv("GEMINI_API_KEY")
        )

        self.vector_store = self._load_or_create_vector_store()

        if self.vector_store:
            self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 5})
            print("✅ RAG System is ready to chat!")
        else:
            self.retriever = None
            print("🛑 No vector store created. Please add documents first.")

    def _validate_api_key(self):
        if not (os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")):
            raise ValueError("🛑 GEMINI_API_KEY not set in .env")

    def _load_or_create_vector_store(self):
        if os.path.exists(config.FAISS_INDEX_PATH):
            print(f"📦 Loading FAISS index from {config.FAISS_INDEX_PATH}")
            return FAISS.load_local(
                config.FAISS_INDEX_PATH,
                self.embedding_model,
                allow_dangerous_deserialization=True,
            )

        print("📁 No index found — creating new…")
        docs = self._get_documents_from_source(config.BOOK_SOURCE_DIR)

        if not docs:
            print("🛑 No document loaded. Add files and restart.")
            return None

        vector_store = FAISS.from_documents(docs, self.embedding_model)
        vector_store.save_local(config.FAISS_INDEX_PATH)
        print("✅ FAISS index created and saved.")
        return vector_store

    def _get_documents_from_source(self, source_path: str) -> List[Document]:
        if not os.path.exists(source_path):
            os.makedirs(source_path, exist_ok=True)
            print("📂 Source folder created. Add files and restart.")
            return []

        files = sorted(os.listdir(source_path))
        if not files:
            print("🛑 Source directory empty. Add documents.")
            return []

        print(f"📚 Scanning {len(files)} files...")
        all_docs = []

        for filename in files:
            file_path = os.path.join(source_path, filename)

            try:
                if filename.lower().endswith(".pdf"):
                    print(f"  📖 PDF: {filename}")
                    elements = partition_pdf(
                        filename=file_path,
                        strategy="hi_res",
                        chunking_strategy="by_title",
                        infer_table_structure=True,
                    )
                    for el in elements:
                        if el.text and el.text.strip():
                            all_docs.append(
                                Document(
                                    page_content=el.text,
                                    metadata={"source": filename, "type": "pdf"},
                                )
                            )

                elif filename.lower().endswith(".txt"):
                    print(f"  📝 TXT: {filename}")
                    with open(file_path, "r", encoding="utf-8") as f:
                        text = f.read()
                        if text.strip():
                            all_docs.append(
                                Document(
                                    page_content=text,
                                    metadata={"source": filename, "type": "txt"},
                                )
                            )

                elif filename.lower().endswith(".xlsx"):
                    print(f"  📊 Excel: {filename}")
                    df = pd.read_excel(file_path, sheet_name=None)
                    for sheet_name, sheet_data in df.items():
                        text = sheet_data.to_string(index=False, header=True)
                        if text.strip():
                            all_docs.append(
                                Document(
                                    page_content=text,
                                    metadata={
                                        "source": filename,
                                        "type": "excel",
                                        "sheet": sheet_name,
                                    },
                                )
                            )

                else:
                    print(f"⚠️ Unsupported file skipped: {filename}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

        print(f"📌 Total documents processed: {len(all_docs)}")
        return all_docs

    def ask(self, question: str):
        if not self.retriever:
            return "🛑 No retriever available. Add documents first."

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            f"Source: {doc.metadata.get('source')} | Type: {doc.metadata.get('type')}\n{doc.page_content}"
            for doc in docs
        )

        prompt = (
            f"{config.RAG_SYSTEM_PROMPT}\n\n"
            f"---CONTEXT---\n{context}\n\n"
            f"---QUESTION---\n{question}"
        )

        try:
            response = self.client.models.generate_content(
                model=config.LLM_MODEL,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"❌ Error generating answer: {e}"

    def start_chat(self):
        if not self.retriever:
            print("🛑 No retriever. Add documents first.")
            return

        print("\n💬 RAG System Ready! Ask anything about your uploaded book.\n")

        while True:
            user_query = input("You: ")
            if user_query.lower() in ["exit", "quit"]:
                print("👋 Goodbye!")
                break

            answer = self.ask(user_query)
            print("\n📘 RAG System:", answer, "\n")


if __name__ == "__main__":
    tutor = RagSystem()
    tutor.start_chat()
