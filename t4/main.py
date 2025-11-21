"""The main module of the assistant bot."""

from typing import NoReturn
from bot__ import (
    parse_input, 
    add_contact, 
    change_contact, 
    output_phone, 
    handler_hello, 
    handler_add, 
    handler_change,
    handler_phone,
    handler_all,
    handler_goodbye,
    COMMANDS
    )

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

            if command in COMMANDS:
                result = COMMANDS[command](args, contacts)
                print(result)
                if command in ['close', 'exit']:
                    break
            else:
                print("Invalid command!")

        except Exception as err:
            print(f"Error: {err}")
                         
if __name__ == "__main__":
    main()