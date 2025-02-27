import os

import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_chroma import Chroma

from helpers import file, prompt


class DocumentChat:
    def __init__(self, model, model_variant):
        """Initialize the document chat system with embeddings and vector store."""

        self.embeddings = model.get_embeddings()

        model_settings = model.get_settings()

        self.vector_store = Chroma(
            embedding_function=self.embeddings,
            persist_directory=file.get_chroma_db_folder(),
            collection_metadata={
                "hnsw:space": "cosine",
                "dimension": model_settings.get("dimension", 0),
            },
        )

        # Initialize model
        self.llm = model.get_model(model_variant)

        # Configure text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=500,
            add_start_index=True,
        )

        # RAG prompt template
        self.prompt = ChatPromptTemplate.from_template(prompt.build())

    def process_uploaded_files(self, uploaded_files):
        """Process and store uploaded files into vectors database only if not already processed."""
        if not uploaded_files:
            return

        for f in uploaded_files:
            if f.name in st.session_state.processed_files:
                continue

            file_path = os.path.join(file.get_uploads_folder(), f.name)

            try:
                with open(file_path, "wb") as fh:
                    fh.write(f.read())

                loader = DirectoryLoader(file.get_uploads_folder())
                documents = loader.load()

                # Convert metadata lists to strings to avoid ChromaDB errors
                for doc in documents:
                    doc.metadata = {
                        key: ", ".join(value) if isinstance(value, list) else value
                        for key, value in doc.metadata.items()
                    }

                chunks = self.text_splitter.split_documents(documents)
                self.vector_store.add_documents(chunks)

                st.session_state.processed_files.add(f.name)

            except Exception as e:
                st.error(f"Error processing file {f.name}: {e}")
            finally:
                os.remove(file_path)

    def clear_all_documents(self):
        """Remove all stored document vectors and uploaded files."""
        try:
            self.vector_store.delete_collection()

            st.session_state.processed_files.clear()
            st.sidebar.success("✅ All documents and vectors have been removed.")
        except Exception as e:
            st.sidebar.error(f"❌ Error clearing documents: {e}")

    def query(self, question: str):
        """Retrieve relevant document context and generate AI response."""
        if not question.strip():
            return "⚠️ Please enter a valid question."

        query_embedding = self.embeddings.embed_query(question)
        docs = self.vector_store.similarity_search_by_vector(query_embedding, k=5)

        if not docs:
            return "I couldn't find relevant information in the documents."

        context = "\n\n".join([doc.page_content for doc in docs])
        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        return response.content.strip()
