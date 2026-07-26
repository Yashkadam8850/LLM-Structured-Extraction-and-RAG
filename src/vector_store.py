import faiss
import numpy as np

def create_vector_store(embeddings):
    """
    Create a FAISS vector index 
    """
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    return index

