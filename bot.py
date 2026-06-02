from intelligence import responder
print ("🤖 DANI started! Type 'quit' to stop. \n")
while True:
    user_input = input("You: ").lower() 

    if user_input == "exit":
        print("🤖 DANI stopped. Goodbye!")
        break

    response = get_responder(user_input)
    print("bot:", response )
