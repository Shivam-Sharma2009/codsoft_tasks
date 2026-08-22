# Simple Rule-Based Chatbot

from datetime import datetime

print("ChatBot: Hi! Type 'bye' to exit.")

while True:
    message = input("You: ").lower().strip()

    if message in ("hi", "hello", "hey"):
        print("Bot: Hello! How can I help?")
    elif "how are you" in message:
        print("Bot: I'm doing well. Thanks!")
    elif "your name" in message:
        print("Bot: I'm RuleBot, a simple rule-based chatbot.")
    elif "help" in message:
        print("Bot: Try asking about my name, date, time, or say hello.")
    elif "time" in message:
        print("Bot:", datetime.now().strftime("%H:%M:%S"))
    elif "date" in message:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))
    elif message == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")
