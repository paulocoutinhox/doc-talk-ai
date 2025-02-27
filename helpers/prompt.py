def build():
    return """\
    You are an expert assistant that answers questions based on uploaded documents. If you don't know the answer, just say that you don't have enough information. Keep the answer concise and clear.

    Context: {context}
    Question: {question}

    Answer:
    """
