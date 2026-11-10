from agent_core.llm import ask_model

def main():
    question = input("Ask the AI something: ")
    answer = ask_model(question)

    print("\nAI response:")
    print(answer)

if __name__ == "__main__":
    main()