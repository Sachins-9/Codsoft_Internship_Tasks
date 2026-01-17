
from datetime import datetime

print("🤖 Hey Hello What's Your Name 😊")
name = input("You: ")

chat_history = [] 

print(f"\nBot: Welcome, {name}!")
print("Bot: How can I help You?")
print("You can use following commands:\n Commands: Study, Project, Joke, Chat History, Help, Exit")

while True:
    user_input = input(f"\n{name}: ").strip()

    chat_history.append(f"You: {user_input}")

    user_input_lower = user_input.lower()

    if user_input_lower == "exit":
        print("Bot: Goodbye 👋")
        chat_history.append("Bot: Goodbye")
        break

    elif user_input_lower == "help":
        response = "I provide study tips, project guidance, joke, and chat history."

    elif user_input_lower == "study":
        response = "Study regularly for short durations to improve understanding."

    elif user_input_lower == "project":
        response = "Choose a small project first and then enhance it step by step."

    elif user_input_lower == "joke":
        response = (
            "😂 Joke 1: Why do programmers hate nature? Too many bugs!\n"
            "😂 Joke 2: Why did the computer go to the doctor? Because it caught a virus!"
        )

    elif user_input_lower == "chat history":
        print("\n📜 Chat History:")
        for msg in chat_history:
            print(msg)
        continue

    else:
        response = "Command not recognized. Type 'help' to see available commands."

    print("Bot:", response)
    chat_history.append("Bot: " + response)
