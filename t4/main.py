"""The main module of the assistant bot."""

from bot__ import parse_input, add_contact, change_contact, output_phone
from typing import NoReturn

def main() -> NoReturn:
    """
    The bot's main cycle: processing user commands.

    Uses a dictionary to store contacts.
    Ends with the commands 'close' or 'exit'.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                print("Please enter a command.")
                continue

            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can i help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone": 
                print(output_phone(args, contacts))
            elif command == "all":
                if not contacts:
                    print("No contacts saved.")
                else:
                    for name, phone in contacts.items():
                        print(name, phone)
            else:
                print("Invalid command!")

        except Exception as err:
            print(f"Error: {err}")
                         
if __name__ == "__main__":
    main()