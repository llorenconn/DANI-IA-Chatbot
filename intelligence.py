import random

def responder(message):
    message = message.lower()

    if "hi" in message or "hello" in message:
        return random.choice([
            "Hi!",
            "Hello! How can I help you today?",
            "Hey! How are you?"
        ])

    if "name" in message:
        return random.choice([
            "I'm Dani 🤖",
            "You can call me Dani.",
            "I'm your friendly chatbot!"
        ])

    if "how are you" in message:
        return random.choice([
            "I'm doing great! Thanks for asking.",
            "I'm here and ready to help!",
            "All systems go! How can I assist you?"
        ])

    if "calculate" in message:
        try:
            expression = message.replace("calculate", "").strip()
            return f"Result: {eval(expression)}"
        except:
            return "I couldn't calculate that."

    try:
        if any(op in message for op in ["+", "-", "*", "/"]):
            return f"Result: {eval(message)}"
    except:
        return "I couldn't calculate that."

    return "I didn't understand that. Try something else!"