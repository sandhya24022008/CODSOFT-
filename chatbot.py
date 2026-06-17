print("=== Simple ChatBot ===")
print("Type 'exit' to stop the chatbot.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you today?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is SmartBot.")

    elif user == "what are you doing":
        print("Bot: I am chatting with you.")

    elif user == "python":
        print("Bot: Python is a popular programming language.")

    elif user == "ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "exit":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
