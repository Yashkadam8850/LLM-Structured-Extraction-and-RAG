from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def split_documents(documents):
    """
    Split documents into smaller chunks.
    """
    splitter= RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=70
    )

    chunks= splitter.create_documents(documents)
    return chunks


def create_embeddings(chunks):
    """
    Generate embeddings for document chunks.
    """

    texts = [chunk.page_content for chunk in chunks]

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True
    )

    return texts, embeddings