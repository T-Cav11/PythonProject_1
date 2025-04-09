bot_name: str = "Cornelius Coconut"
print(f"Hello there! I am {bot_name} and I am here to assist you. How can I help you today?")

while True:
    user_input: str = input("You: ").lower()

    if user_input in ["hi", "hello"]:
        print(f"{bot_name}: Howdy partner! How may I assist you today?")
    elif user_input in ["bye", "goodbye", "see you later"]:
        print(f"{bot_name}: Catch ya later partner x")
    elif user_input in ["thanks", "thank you"]:
        print("No worries sexy xoxo")
    elif user_input in ["+", "add"]:
        print(f"{bot_name}: Sure thing bud. Lets do that")
        try:
            num1: float = float(input("First number: "))
            num2: float = float(input("Second number: "))
            print(f"{bot_name}: The sum is {num1+num2}")
        except ValueError:
            print(f"{bot_name}: Oops! That doesn't work. Try again with a valid number")
    else:
        print("Sorry I didn't understand that one. Tim Cheese has removed that part of my brain")