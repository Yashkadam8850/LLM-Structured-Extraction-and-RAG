def retrieve(query_embedding, index, texts, top_k=3):
    distances, indices = index.search(query_embedding, top_k)

    retrieved = []

    for idx in indices[0]:
        retrieved.append(texts[idx])

    return retrieved