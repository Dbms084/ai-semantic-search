"""RAG-powered document question answering."""

from app.rag.answer_generator import generate_answer


def main():
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        answer = generate_answer(query)
        print("\nAnswer:")
        print(answer)
        print("-" * 80)


if __name__ == "__main__":
    main()
