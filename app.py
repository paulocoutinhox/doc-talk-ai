import streamlit as st

from helpers import file, model
from lang_chain.document_chat import DocumentChat

# General
file.create_uploads_folder()


# Sidebar - Application title
st.sidebar.title("DOC TALK - AI 🧠")


# Sidebar - AI Model Selection
st.sidebar.subheader("🤖 AI Model")

models = model.load_models()

if not models:
    st.sidebar.error("❌ No models available, please add models.")
    st.stop()

model_names = [model.name() for model in models]
selected_model_name = st.sidebar.selectbox("Select AI Model:", model_names)
selected_model = next((m for m in models if m.name() == selected_model_name), None)

model_variants = selected_model.get_variants()

if model_variants:
    variant_keys = list(model_variants.keys())
    default_variant = selected_model.get_default_variant()

    # Pre-select the default variant if available
    selected_model_variant = st.sidebar.selectbox(
        "Select Model Variant:",
        variant_keys,
        format_func=lambda key: model_variants[key],
        index=(
            variant_keys.index(default_variant)
            if default_variant in variant_keys
            else 0
        ),
    )
else:
    selected_model_variant = selected_model.get_default_variant()


# Instantiate DocumentChat
document_chat = DocumentChat(
    model=selected_model,
    model_variant=selected_model_variant,
)


# Sidebar - Document Upload
st.sidebar.subheader("📂 Upload Documents")
uploaded_files = st.sidebar.file_uploader(
    "Upload files (PDF, TXT, MD, DOCX, XLSX, CSV, EPUB)",
    accept_multiple_files=True,
)


# Initialize session state for document tracking
st.session_state.setdefault("processed_files", set())


# Process uploaded documents
if uploaded_files:
    document_chat.process_uploaded_files(uploaded_files)
    st.sidebar.success("✅ Documents uploaded and processed!")


# Sidebar - Remove All Documents Button
if st.sidebar.button("🗑️ Clear All Documents & Vectors"):
    document_chat.clear_all_documents()


# Main Area - User prompt
st.header("💬 Ask Something About Your Documents")
user_prompt = st.text_input("Enter your question below:")

if st.button("🚀 Generate"):
    if not user_prompt:
        st.warning("⚠️ Please enter a question.")
    else:
        try:
            query_response = document_chat.query(user_prompt)

            if query_response.startswith("I couldn't find"):
                st.warning(query_response)
            else:
                st.divider()
                st.subheader("🧠 AI Response")
                st.write(query_response)
        except ValueError as e:
            st.error(f"❌ Error: {str(e)}")
