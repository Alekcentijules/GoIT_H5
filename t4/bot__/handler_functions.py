from .processor_functions import add_contact, change_contact, output_phone

def handler_hello(args, contacts):
    return 'How can I help you?'

def handler_add(args, contacts):
    return add_contact(args, contacts)

def handler_change(args, contacts):
    return change_contact(args, contacts)

def handler_phone(args, contacts):
    return output_phone(args, contacts)

def handler_all(args, contacts):
    if not contacts:
        return 'No contacts saved.'
    return "\n".join(f"{name}: {contact}" for name, contact in contacts.items())

def handler_goodbye(args, contacts):
    return 'Good bye!'

COMMANDS = {
    'hello': handler_hello,
    'add': handler_add,
    'change': handler_change,
    'phone': handler_phone,
    'all': handler_all,
    'close': handler_goodbye,
    'exit': handler_goodbye
}