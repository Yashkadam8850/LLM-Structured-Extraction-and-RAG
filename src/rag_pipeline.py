import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

from src.embeddings import split_documents, create_embeddings
from src.vector_store import create_vector_store
from src.retrieval import retrieve
from sentence_transformers import SentenceTransformer

load_dotenv()

client = OpenAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    base_url="https://api.mistral.ai/v1"
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents(folder="data/documents"):
    documents = []

    for file in sorted(Path(folder).glob("*.txt")):
        with open(file, "r", encoding="utf-8") as f:
            documents.append(f.read())

    return documents


def build_rag():

    docs = load_documents()

    chunks = split_documents(docs)

    texts, embeddings = create_embeddings(chunks)

    index = create_vector_store(embeddings)

    return texts, index


def ask_question(question):

    texts, index = build_rag()

    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    retrieved = retrieve(
        query_embedding,
        index,
        texts,
        top_k=3
    )

    context = "\n\n".join(retrieved)

    prompt = f"""
Answer the question ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    return retrieved, answer


if __name__ == "__main__":

    retrieved, answer = ask_question(
        "What is Prompt Engineering?"
    )

    print("\nRetrieved Chunks:\n")

    for chunk in retrieved:
        print("-" * 60)
        print(chunk)

    print("\nAnswer:\n")
    print(answer)
    