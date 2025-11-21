"""Bot assistant package."""

from .processor_functions import add_contact, change_contact, output_phone
from .command_parser import parse_input
from .handler_functions import (
    handler_hello,
    handler_add,
    handler_change,
    handler_phone,
    handler_all,
    handler_goodbye,
    COMMANDS
)