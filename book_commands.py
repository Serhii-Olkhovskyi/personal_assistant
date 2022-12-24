# All ContactBook functions

from book_class import Record, Address, Email, Birthday


def name_input():
    name = input(f'Please enter contact name: ')
    return name


def address_input():
    address = input(f'Please enter contact address: ')
    return address


def phones_input():
    phones = input(f'Please enter contact phones: ')
    return phones.split()


def email_input():
    email = input(f'Please enter contact email: ')
    return email


def birthday_input():
    birthday = input(f'Please enter contact birthday: ')
    return birthday


# @input_error
def hello_func():
    """
    Hello Bot message
    :return: answer = string
    """
    pass


# @input_error
def add_contact_func(contacts):
    '''
    Command for adding records to the dictionary
    :param command: user input
    :return: string
    '''

    name = name_input()
    address = address_input()
    phones = phones_input()
    email = email_input()
    birthday = birthday_input()

    if name not in contacts.data.keys():
        contacts.add_record(Record(name))
        if phones:
            for phone in phones:
                if phone not in contacts[name].get_phones():
                    contacts[name].add_phone(phone)

        if address:
            contacts[name].address = Address(address)

        if email:
            contacts[name].email = Email(email)

        if birthday:
            contacts[name].birthday = Birthday(birthday)

        return f"Contact {name} was added with: phones:[{', '.join(phones)}], address: {address}, email: {email}, birthday: [{birthday}]"


# @input_error
def add_phone_func(contacts):
    '''
    Command for adding phones to the contact
    :param command: contact book
    :return: string
    '''

    name = name_input()
    phones = phones_input()

    if name in contacts.data.keys():
        if phones:
            for phone in phones:
                if phone not in contacts[name].get_phones():
                    contacts[name].add_phone(phone)
                return f"Phones:[{', '.join(phones)}] were added to contact '{name}'."
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add phone.")


def add_address_func(contacts):
    '''
    Command for adding address to the contact
    :param command: contact book
    :return: string
    '''

    name = name_input()
    address = address_input()

    if name in contacts.data.keys():
        if address:
            if not contacts[name].address:
                contacts[name].add_address(address)
                return f"Address:{address}] was added to contact '{name}'."
            else:
                raise ValueError(f"Contact '{name}' already has address record. Please enter another command to "
                                 f"change address.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add address.")


def add_email_func(contacts):
    '''
    Command for adding address to the contact
    :param command: contact book
    :return: string
    '''

    name = name_input()
    email = email_input()

    if name in contacts.data.keys():
        if email:
            if not contacts[name].email:
                contacts[name].add_email(email)
                return f"Email:{email} was added to contact '{name}'."
            else:
                raise ValueError(f"Contact '{name}' already has email record. Please enter another command to "
                                 f"change email.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add email.")


def add_birthday_func(contacts):
    '''
    Command for adding address to the contact
    :param command: contact book
    :return: string
    '''

    name = name_input()
    birthday = birthday_input()

    if name in contacts.data.keys():
        if birthday:
            if not contacts[name].birthday:
                contacts[name].add_birthday(birthday)
                return f"Birthday:{birthday} was added to contact '{name}'."
            else:
                raise ValueError(f"Contact '{name}' already has address record. Please enter another command to "
                                 f"change birthday.")
    else:
        raise KeyError(f"No records with '{name}' contact found. Type another contact name to add birthday.")


# @input_error
def exit_func():
    """
    "good bye", "close", "exit" on any of these commands,
    the bot terminates its work after it displays "Good bye!" in the console.
    :return: string
    """
    return "Good bye!"


# @input_error
def save_contacts_to_file(contacts):
    """
    Function saves contacts to file
    :return: string
    """
    contacts.save_to_file()
    return "Contacts have been saved successfully."


# @input_error
def load_contacts_from_file(contacts):
    """
    Function loads contacts from the file
    :return: string
    """
    contacts.read_from_file()
    return "Contacts have been loaded successfully."

