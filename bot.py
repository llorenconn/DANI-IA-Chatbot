from intelligence import responder

print("🤖 Mini AI started! Type 'exit' to quit.\n")

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("Bot: See you later!")
        break

    response = responder(msg)
    print("Bot:", response)
    