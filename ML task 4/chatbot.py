def chatbot_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hello! How can I help you?"
    elif "internship" in message:
        return "This internship focuses on Machine Learning model implementation."
    elif "task" in message:
        return "Task-4 is about building a predictive ML model."
    elif "bye" in message:
        return "Goodbye! Best of luck with your internship 😊"
    else:
        return "Sorry, I didn't understand that."
