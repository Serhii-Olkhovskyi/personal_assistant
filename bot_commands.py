# Bot commands associated with ContactBook, Notes, Sort folders

import book_commands
from help import all_commands

# Bot commands with associated functions
COMMANDS = {
    'hello': book_commands.hello_func,
    'exit': book_commands.exit_func,
    'close': book_commands.exit_func,
    'good bye': book_commands.exit_func,
    'add contact': book_commands.add_contact_func,
    'help': all_commands,
    # 'change contact': change,
    # 'delete contact': delete_phone,
    # 'show all contacts': show_all,
    # 'phone': phone,
    # 'birthday': show_birthday,
    # 'save': save_contacts_to_file,
    # 'load': load_contacts_from_file,
    # 'search': find_contacts
}
