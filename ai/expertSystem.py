problem_dict = {
    "Printer not working" : "Check that it is turned on and connected to the network",
    "Can't log in" : "Make sure youre using the correct username and password",
    "Software not installing " : "Check that your system meets the sytem requirements ",
    "Internet connection not working " : "Restart your modem or router",
    "Email not sending" : "Check that you're using the correct email server settings"
}

def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry ,I dont know how to help with the problem."

while True:
    user_input = input("What's the problem? Type 'exit' to quit.")
    response = handle_request(user_input) 
      