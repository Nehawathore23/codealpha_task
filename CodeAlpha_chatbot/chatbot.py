
from responses import responses

def get_response(user_input):
    """Return chatbot response using dictionary + extra rules."""

    user_input = user_input.lower()

    if "time" in user_input:
        return "I cannot tell the time yet!"
    elif "country" in user_input:
        return "I am AI, so I don't belong to any country!"
    elif "joke" in user_input:
        return "Why don't robots get hungry? Because they have mega-bytes! 🤖"

    else:
        return responses.get(user_input, "Sorry, I don't understand that.")


def start_chatbot():
    """Main loop for the chatbot."""

    print("🤖 PyBot: Hello! I'm PyBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("PyBot: Goodbye! Have a great day! 😊")
            break

        reply = get_response(user_input)
        print("PyBot:", reply)
