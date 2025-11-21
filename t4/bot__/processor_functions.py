"""Module with command processing functions."""
from functools import wraps
from typing import List, Dict, Callable

Contacts = Dict[str, str]
def input_error(func: callable) -> Callable:
    """
    Decorator for handling errors in commands.

    Args:
        func (Callable): Command handler.

    Returns:
        Callable: Wrapped function.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments."
        except Exception as err:
            return f"Error: {err}"
    return inner

@input_error
def add_contact(args: List[str], contacts: Contacts) -> str:
    """
    Adds a new contact.

    Args:
        args (List[str]): List of arguments: [name, phone]
        contacts (Dict[str, str]): Dictionary of contacts

    Returns:
        str: Message about the result
    """
    name, phone = args
    if not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    elif name in contacts:
        return "This contact was add."
    contacts[name] = phone
    return "Contact added!"

@input_error
def change_contact(args: List[str], contacts: Contacts) -> str:
    """
    Changes the number of an existing contact.

    Args:
        args (List[str]): [name, new_number]
        contacts (Dict[str, str]): Dictionary of contacts

    Returns:
        str: Message about the result
    """
    name, phone = args
    if name not in contacts:
        return "This contact isn't in list."
    elif not phone.isdigit():
        return "When adding a phone number, only digits should be entered."
    contacts[name] = phone
    return "Contact changed!"

@input_error
def output_phone(args: List[str], contacts: Contacts) -> str:
    """
    Displays the phone number by name.

    Args:
        args (List[str]): [name]
        contacts (Dict[str, str]): Contact dictionary

    Returns:
        str: Phone number or error message
    """
    name = args[0]
    return contacts[name]
