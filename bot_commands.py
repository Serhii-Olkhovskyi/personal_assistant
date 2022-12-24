# Bot commands associated with ContactBook, Notes, Sort folders

import book_commands


# Bot commands with associated functions
COMMANDS = {
    'hello': book_commands.hello_func,
    'exit': book_commands.exit_func,
    'close': book_commands.exit_func,
    'good bye': book_commands.exit_func,
    'add contact': book_commands.add_contact_func,
    'add phone': book_commands.add_phone_func,
    'add address': book_commands.add_address_func,
    'add email': book_commands.add_email_func,
    'add birthday': book_commands.add_birthday_func,
    # 'change contact': change,
    # 'delete contact': delete_phone,
    # 'show all contacts': show_all,
    # 'phone': phone,
    # 'birthday': show_birthday,
    'save': book_commands.save_contacts_to_file,
    'load': book_commands.load_contacts_from_file,
    # 'search': find_contacts
}