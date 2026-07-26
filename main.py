from src.validation import validate_all, save_results
from src.rag_pipeline import ask_question

def run_structured_extraction():
    valid_records, errors = validate_all()
    save_results(valid_records, errors)

    print("Structured Extraction Completed.")
    print(f"Valid Records: {len(valid_records)}")
    print(f"Validation Errors: {len(errors)}")


def run_rag_demo():
    queries = [
        "What is Artificial Intelligence?",
        "Explain Machine Learning.",
        "What is Deep Learning?",
        "What is Generative AI?",
        "What is Prompt Engineering?"
    ]

    for query in queries:
        print("=" * 80)
        print("Question:", query)

        retrieved, answer = ask_question(query)

        print("\nRetrieved Chunks:")
        for chunk in retrieved:
            print("-" * 40)
            print(chunk[:250], "...\n")

        print("Answer:")
        print(answer)
        print()


if __name__ == "__main__":

    run_structured_extraction()

    print("\n")

    run_rag_demo()