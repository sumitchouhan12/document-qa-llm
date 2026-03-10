import streamlit as st
from utils.loader import load_pdf
from utils.qa_chain import create_qa_chain

st.title("AI Document Question Answering")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_pdf("data/temp.pdf")

    retriever, generator = create_qa_chain(docs)

    question = st.text_input("Ask a question about the document")

    if question:

        context_docs = retriever.invoke(question)

        context = "\n".join([doc.page_content for doc in context_docs])

        prompt = f"""
        Use the context below to answer the question.

        Context:
        {context}

        Question:
        {question}
        """

        answer = generator(prompt)[0]["generated_text"]

        st.write("Answer:")
        st.write(answer)